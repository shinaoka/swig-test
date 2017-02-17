//#pragma once

//#include <time.h>
//extern double My_variable;
  
//int fact(int n);
 //
//int my_mod(int x, int y);
    //
//char *get_time();

//class AAA {
    //int i;
//};

template<class T> class List {};

#ifdef SWIG
%template(intList) List<int>;
%template(doubleList) List<double>;
#endif
