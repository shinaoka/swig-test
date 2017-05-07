/* example_B.i */
%module example_B
%{
#define SWIG_FILE_WITH_INIT
#include "example_B.hpp"
%}

%include "example_B.hpp"

%template(real_tB) tB<double>;
