#pragma once

#include <vector>
#include <iostream>
//#include <alps/gf/gf.hpp>
#include <complex>
#include <Eigen/Core>
#include <Eigen/CXX11/Tensor>
#include <boost/multi_array.hpp>

#include "example_B.hpp"

/* */

typedef std::complex<double> dcomplex;

double drms(const std::vector<double>& seq);
dcomplex crms(const std::vector<dcomplex>& seq);

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

inline void process_B(const B& b) {
    //do nothing
}

template<typename T>
void process_tB(const tB<T>& b) {
    //do nothing
    std::cout << "process_tB" << std::endl;
}

inline void read_array(const boost::multi_array<double,4,std::allocator<double> >& in) {
}

inline Eigen::Tensor<double,4> gen_eigen_tensor() {
    Eigen::Tensor<double,4> tmp(4,4,4,4);
    tmp.setConstant(1.0);
    for (int i=0; i<4; ++i) {
        tmp(i,0,0,0) = i;
    }
    return tmp;
}

inline void read_write_array(Eigen::Tensor<double,2>& in) {
    in = Eigen::Tensor<double,2>(2,2);
    in.setZero();
    std::cout << "in " <<  in(0,0) << std::endl;
    in(0,0) = 1000;
}
