/* example.i */
%module example
%{
#define SWIG_FILE_WITH_INIT
#include "example.hpp"
%}

%include "typemaps.i"
%include "numpy.i"
%include "std_vector.i"

%init %{
import_array();
%}

%include "multi_array.i"

%multi_array_typemaps(std::vector<double>);
%multi_array_typemaps(std::vector<std::complex<double> >);

/*
%rename(drms) rms(std::vector<double>&);
%rename(crms) rms(std::vector<dcomplex>&);
*/

%include "example.hpp"

