swig -c++ -python example.i 
clang++ -c example.cpp  example_wrap.cxx -I /opt/local/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7
clang++ -shared example.o example_wrap.o -L/opt/local/lib -lpython2.7 -o _example.so 
