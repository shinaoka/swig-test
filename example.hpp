#include <vector>
//#include <alps/gf/gf.hpp>
#include <complex>
#include <Eigen/Core>

/*
namespace alps {
    class B {
        public:
        double operator()() {return 0.0;}
        double do_job();
    };
    namespace gf {
        template<class T> class Array {
            public:
            Array(int N) : array_(N) {}
        
            const T& operator()(int i) const {return array_[i];}
            T& operator()(int i) {return array_[i];}
        
            private:
            std::vector<T> array_;
        };
    }
}
*/

typedef std::complex<double> dcomplex;

//double rms(double* seq, int n);
//double rms(std::vector<double>& seq, int n);
double drms(const std::vector<double>& seq);
dcomplex crms(const std::vector<dcomplex>& seq);
//std::complex<double> crms(std::complex<double>* seq, int n);
//std::complex<double> crms(std::complex<double>& seq, int n);

//template<class T> class List {};
//
typedef Eigen::Matrix<double,Eigen::Dynamic,Eigen::Dynamic> matrix_t;

inline Eigen::Matrix<double,Eigen::Dynamic,Eigen::Dynamic>
gen_matrix() {
    Eigen::Matrix<double,Eigen::Dynamic,Eigen::Dynamic> m(10,2);
    m.setZero();
    for (int i=0; i<m.rows(); ++i) {
        m(i,0) = i;
    }
    return m;
}


#ifdef SWIG
//%template(intList) List<int>;
//%template(doubleList) List<double>;
//%template(doubleArray) Array<double>;
//%template(LegendreGF) alps::gf::one_index_gf< std::complex<double>, alps::gf::legendre_mesh >;
//%template(OmegaGF) alps::gf::one_index_gf<std::complex<double>, alps::gf::matsubara_mesh<mesh::POSITIVE_ONLY> >;
#endif
