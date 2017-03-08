#include <vector>
#include <alps/gf/gf.hpp>

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

//double rms(double* seq, int n);
//template<class T> class List {};


#ifdef SWIG
//%template(intList) List<int>;
//%template(doubleList) List<double>;
//%template(doubleArray) Array<double>;
%template(LegendreGF) alps::gf::one_index_gf< std::complex<double>, alps::gf::legendre_mesh >;
%template(OmegaGF) alps::gf::one_index_gf<std::complex<double>, alps::gf::matsubara_mesh<mesh::POSITIVE_ONLY> >;
#endif
