/* example.i */
%module example
%{
#define SWIG_FILE_WITH_INIT
#include <vector>
%}

%include "typemaps.i"
%include "numpy.i"
%include "std_vector.i"

%init %{
  import_array();
%}

%fragment("Array_Fragments", "header", fragment="NumPy_Fragments")
%{
  template <typename T> int NumPyType() {return -1;};
  template<> int NumPyType<double>() {return NPY_DOUBLE;};
  template<> int NumPyType<std::complex<double> >() {return NPY_CDOUBLE;};
  template<> int NumPyType<int>() {return NPY_INT;};

  template <typename T>
  struct CXXTypeTraits {
    typedef double scalar;
    static int dim();
    static int size(const T& obj, int i);
    static bool resize(T& obj, const std::vector<int>& sizes);
    static void set_zero(T& obj); 
    static scalar& element_at(T& obj, const std::vector<int>& indices);
  };

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


  template <class A>
  bool ConvertFromNumpy(A* out, PyObject* in)
  {
    typedef CXXTypeTraits<A> traits;
    typedef typename traits::scalar scalar;

    // Check object type
    if (!is_array(in))
    {
      PyErr_SetString(PyExc_ValueError, "The given input is not known as a NumPy array or matrix.");
      return false;
    }

    // Check data type
    if (array_type(in) != NumPyType<scalar>())
    {
      PyErr_SetString(PyExc_ValueError, "Type mismatch between NumPy and C++ objects.");
      return false;
    }

    // Check dimensions
    if (array_numdims(in) != traits::dim())
    {
      PyErr_SetString(PyExc_ValueError, "Dimension mismatch between NumPy and C++ objects.");
      return false;
    }

    const int dim = traits::dim();

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

    //FIXME: CHECK THIS
    //traits::set_zero(*out, data_size);
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


%}

%define %multi_array_typemaps(CLASS...)
// In: const&
%typemap(in, fragment="Array_Fragments") CLASS const& (CLASS tempp)
{
  // In: const&
  if (!ConvertFromNumpy<CLASS >(&tempp, $input))
    SWIG_fail;
  $1 = &tempp;
}
%enddef
