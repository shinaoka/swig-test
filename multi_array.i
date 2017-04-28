%{
#define SWIG_FILE_WITH_INIT
#include <vector>
#include "Eigen/Core"
%}

%include "typemaps.i"
%include "numpy.i"
%include "std_vector.i"

%init %{
  import_array();
%}

%fragment("Array_Fragments", "header", fragment="NumPy_Fragments")
%{
  template <typename T> int num_py_type() {return -1;};
  template<> int num_py_type<double>() {return NPY_DOUBLE;};
  template<> int num_py_type<std::complex<double> >() {return NPY_CDOUBLE;};
  template<> int num_py_type<int>() {return NPY_INT;};

  template <typename OBJ>
  struct CXXTypeTraits {
    typedef double scalar;
    static int dim();
    static int size(const OBJ& obj, int i);
    static bool resize(OBJ& obj, const std::vector<int>& sizes);
    static void set_zero(OBJ& obj); 
    static scalar& element_at(OBJ& obj, const std::vector<int>& indices);
  };

  template<typename S, typename T>
  void copy_data_to_numpy(std::vector<int>& data_size, S* out, T* in);

/*
  template <typename OBJ>
  struct element_at {
    static typename CXXTypeTraits<OBJ>::scalar& at(OBJ& obj, const std::vector<int>& indices);
  };
*/

  template <typename S>
  struct CXXTypeTraits<std::vector<S> > {
    typedef S scalar;
    typedef std::vector<S> obj_type;
    static int dim() { return 1;};
    static int size(const obj_type& obj, int i) {
      assert(i==0);
      return obj.size();
    }
    static bool resize(obj_type& obj, const std::vector<int>& sizes) {
      assert(sizes.size()==dim());
      obj.resize(sizes[0]);
      return true;
    }
    static void set_zero(obj_type& obj) {
      std::fill(obj.begin(), obj.end(), static_cast<S>(0.0));
    } 
    static scalar& element_at(obj_type& obj, const std::vector<int>& indices) {
      assert(indices.size()==1 && indices[0] < obj.size());
      return obj[indices[0]];
    }
  };

/*
  template <typename S>
  struct element_at<std::vector<S> > {
    typedef std::vector<S> OBJ;
    static S& at(OBJ& obj, const std::vector<int>& indices) {
      assert(indices.size()==1 && indices[0] < obj.size());
      return obj[indices[0]];
    }
  };
*/

  //template <typename Derived>
  template <typename S, int RowsAtCompileTime, int ColsAtCompileTime>
  struct CXXTypeTraits<Eigen::Matrix<S,RowsAtCompileTime,ColsAtCompileTime> > {
    typedef S scalar;
    typedef Eigen::Matrix<S,RowsAtCompileTime,ColsAtCompileTime> obj_type;
    static int dim() {
      return 2;
    };
    static int size(const obj_type& obj, int i) {
      assert(i<=1);
      if (i==0) {
        return obj.rows();
      } else {
        return obj.cols();
      }
    }
    static bool resize(obj_type& obj, const std::vector<int>& sizes) {
      assert(sizes.size()==dim());
      bool dynamic_row = RowsAtCompileTime == Eigen::Dynamic;
      bool dynamic_col = ColsAtCompileTime == Eigen::Dynamic;
      if (dynamic_row && dynamic_col) {
        //dynamic matrix
        obj.resize(sizes[0], size[1]);
      } else if (!dynamic_row && !dynamic_col) {
        if (RowsAtCompileTime == size[0] && ColsAtCompileTime == size[1]) {
          return true;
        }
        return false;
      } else {
        //FIXME: RESIZABLE?
        return false;
      }
      return true;
    }
    static void set_zero(obj_type& obj) {
      obj.setZero();
    } 
    static scalar& element_at(obj_type& obj, const std::vector<int>& indices) {
      assert(indices.size()==2);
      return obj(indices[0], indices[1]);
    }
  };

/*
  template <typename S, int RowsAtCompileTime, int ColsAtCompileTime>
  struct element_at<Eigen::Matrix<S,RowsAtCompileTime,ColsAtCompileTime> > {
    typedef Eigen::Matrix<S,RowsAtCompileTime,ColsAtCompileTime> OBJ;
    static S& at(OBJ& obj, const std::vector<int>& indices) {
      assert(indices.size()==1 && indices[0] < obj.size());
      return obj[indices[0]];
    }
  };
*/


  template <class A>
  bool ConvertFromNumpyToCXX(A* out, PyObject* in)
  {
    typedef CXXTypeTraits<A> traits;
    typedef typename traits::scalar scalar;
    const int dim = traits::dim();

    // Check object type
    if (!is_array(in))
    {
      PyErr_SetString(PyExc_ValueError, "Input is not as a numpy array or matrix.");
      return false;
    }

    // Check data type
    if (array_type(in) != num_py_type<scalar>())
    {
      PyErr_SetString(PyExc_ValueError, "Type mismatch between numpy and C++ objects.");
      return false;
    }

    // Check dimensions
    if (array_numdims(in) != traits::dim())
    {
      PyErr_SetString(PyExc_ValueError, "Dimension mismatch between numpy and C++ objects.");
      return false;
    }

    std::vector<int> data_size(dim);
    bool resize_required = false;
    for (int i=0; i<dim; ++i) {
      data_size[i] = array_size(in,i);
      resize_required = resize_required || (traits::size(*out,i) < data_size[i]);
    }

    if (resize_required) {
      if (!traits::resize(*out, data_size)) {
        PyErr_SetString(PyExc_ValueError, "Failed to resize C++ object.");
        return false;
      }
    }
    
    // Extract data
    int isNewObject = 0;
    PyArrayObject* temp = obj_to_array_contiguous_allow_conversion(in, array_type(in), &isNewObject);
    if (temp == NULL)
    {
      PyErr_SetString(PyExc_ValueError, "Impossible to convert the input into a Python array object.");
      return false;
    }

    traits::set_zero(*out);

    scalar* data = static_cast<scalar*>(PyArray_DATA(temp));

    int lin_idx = 0;
    std::vector<int> indices(dim);
    if (dim==1) {
      for (int i = 0; i < data_size[0]; ++i) {
        indices[0] = i;
        traits::element_at(*out, indices) = data[lin_idx];
        ++lin_idx;
      }
    } else if (dim==2) {
      for (int i = 0; i < data_size[0]; ++i) {
        for (int j = 0; j < data_size[1]; ++j) {
          indices[0] = i;
          indices[1] = j;
          traits::element_at(*out, indices) = data[lin_idx];
          ++lin_idx;
        }
      }
    }

    return true;
  };

  // Copy elements in C++ object into an existing numpy object
  template <class A>
  bool CopyFromCXXToNumPyArray(PyObject* out, A* in)
  {
    typedef CXXTypeTraits<A> traits;
    typedef typename traits::scalar scalar;
    const int dim = traits::dim();

    // Check object type
    if (!is_array(out))
    {
      PyErr_SetString(PyExc_ValueError, "The given input is not known as a NumPy array or matrix.");
      return false;
    }

    // Check data type
    if (array_type(out) != num_py_type<scalar>())
    {
      PyErr_SetString(PyExc_ValueError, "Type mismatch between NumPy and C++ objects.");
      return false;
    }

    // Check dimensions
    if (array_numdims(out) != traits::dim())
    {
      PyErr_SetString(PyExc_ValueError, "Dimension mismatch between NumPy and C++ objects.");
      return false;
    }

    // Check sizes
    std::vector<int> data_size(dim);
    bool size_mismatch = false;
    for (int i=0; i<dim; ++i) {
      data_size[i] = array_size(out,i);
      size_mismatch = size_mismatch || (traits::size(*in,i) != data_size[i]);
      std::cout << " debug " << i << " " << traits::size(*in,i) << " " << data_size[i] << std::endl;
    }
    if (size_mismatch) {
      PyErr_SetString(PyExc_ValueError, "Dimension mismatch between NumPy and C++ object (return argument).");
      return false;
    }

    // Extract data
    int isNewObject = 0;
    PyArrayObject* temp = obj_to_array_contiguous_allow_conversion(out, array_type(out), &isNewObject);
    //CORRECT?
    if (temp == NULL || isNewObject != 0) {
      PyErr_SetString(PyExc_ValueError, "Impossible to convert the input into a Python array object.");
      return false;
    }

    scalar* data = static_cast<scalar*>(PyArray_DATA(temp));

    copy_data_to_numpy(data_size, data, in);

/*
    int lin_idx = 0;
    std::vector<int> indices(dim);
    if (dim==1) {
      for (int i = 0; i < data_size[0]; ++i) {
        indices[0] = i;
        data[lin_idx] = traits::element_at(*in, indices);
        ++lin_idx;
      }
    } else if (dim==2) {
      for (int i = 0; i < data_size[0]; ++i) {
        for (int j = 0; j < data_size[1]; ++j) {
          indices[0] = i;
          indices[1] = j;
          data[lin_idx] = traits::element_at(*in, indices);
          ++lin_idx;
        }
      }
    }
*/

    return true;
  };

  template <class A>
  bool ConvertFromCXXToNumPyArray(PyObject** out, A* in)
  {
    typedef CXXTypeTraits<A> traits;
    typedef typename traits::scalar scalar;
    const int dim = traits::dim();

    std::vector<npy_intp> dims(dim);
    for (int i=0; i<dim; ++i) {
      dims[i] = traits::size(*in,i);
    }

    *out = PyArray_SimpleNew(2, &dims[0], num_py_type<scalar>());
    if (!out) {
      return false;
    }
    scalar* data = static_cast<scalar*>(PyArray_DATA((PyArrayObject*) *out));


    std::vector<int> data_size(dim);
    for (int i=0; i<dim; ++i) {
      data_size[i] = traits::size(*in,i);
    }

    copy_data_to_numpy(data_size, data, in);

/*

    int lin_idx = 0;
    std::vector<int> indices(dim);
    if (dim==1) {
      for (int i = 0; i < data_size[0]; ++i) {
        indices[0] = i;
        data[lin_idx] = traits::element_at(*in, indices);
        ++lin_idx;
      }
    } else if (dim==2) {
      for (int i = 0; i < data_size[0]; ++i) {
        for (int j = 0; j < data_size[1]; ++j) {
          indices[0] = i;
          indices[1] = j;
          data[lin_idx] = traits::element_at(*in, indices);
          ++lin_idx;
        }
      }
    }
*/

    return true;
  };

  template<typename S, typename T>
  void copy_data_to_numpy(std::vector<int>& data_size, S* out, T* in) {
    typedef CXXTypeTraits<T> traits;
    const int dim = data_size.size();

    int lin_idx = 0;
    std::vector<int> indices(dim);
    if (dim==1) {
      for (int i = 0; i < data_size[0]; ++i) {
        indices[0] = i;
        out[lin_idx] = traits::element_at(*in, indices);
        ++lin_idx;
      }
    } else if (dim==2) {
      for (int i = 0; i < data_size[0]; ++i) {
        for (int j = 0; j < data_size[1]; ++j) {
          indices[0] = i;
          indices[1] = j;
          out[lin_idx] = traits::element_at(*in, indices);
          ++lin_idx;
        }
      }
    }
  }


%}

%define %multi_array_typemaps(CLASS...)
// In: (nothing: no constness)
%typemap(in, fragment="Array_Fragments") CLASS (CLASS temp)
{
  if (!ConvertFromNumpyToCXX<CLASS >(&temp, $input))
    SWIG_fail;
  $1 = temp;
}

// In: const&
%typemap(in, fragment="Array_Fragments") CLASS const& (CLASS temp)
{
  // In: const&
  if (!ConvertFromNumpyToCXX<CLASS >(&temp, $input))
    SWIG_fail;
  $1 = &temp;
}

// Out: (nothing: no constness)
%typemap(out, fragment="Array_Fragments") CLASS
{
  if (!ConvertFromCXXToNumPyArray<CLASS >(&$result, &$1))
    SWIG_fail;
}

%enddef
