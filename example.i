/* example.i */
%module example
%{
#define SWIG_FILE_WITH_INIT
#include "example.hpp"
#include <Eigen/Core>
#include <boost/multi_array.hpp>
%}

%include "typemaps.i"
%include "numpy.i"
%include "std_vector.i"
%include <Eigen/Core>
/*
%include <boost/multi_array.hpp>
*/

%init %{
import_array();
%}

%include "multi_array.i"

%multi_array_typemaps(std::vector<double>);
%multi_array_typemaps(std::vector<std::complex<double> >);
%multi_array_typemaps(Eigen::MatrixBase<Eigen::Matrix<double,Eigen::Dynamic,Eigen::Dynamic> >);
%multi_array_typemaps(Eigen::Matrix<double,Eigen::Dynamic,Eigen::Dynamic>);
%multi_array_typemaps(boost::multi_array<double,4,std::allocator<double> >);

/*
%multi_array_typemaps(Eigen::Matrix<double,Eigen::Dynamic,Eigen::Dynamic>);
*/

/*
%rename(drms) rms(std::vector<double>&);
%rename(crms) rms(std::vector<dcomplex>&);
*/

%include "example.hpp"

