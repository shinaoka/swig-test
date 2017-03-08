/* example.i */
%module example
%{
#define SWIG_FILE_WITH_INIT
#include "example.hpp"
%}

%include "numpy.i"

%init %{
import_array();
%}

%apply (double* IN_ARRAY1, int DIM1) {(double* seq, int n)};

%include "/opt/ALPSCore/include/alps/gf/gf.hpp"
%include "/opt/ALPSCore/include/alps/gf/mesh.hpp"
%include "example.hpp"
