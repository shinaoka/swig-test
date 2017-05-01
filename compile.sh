swig -v -I/opt/Eigen3/include/eigen3 -I/opt/Eigen3/include/eigen3/unsupported -I/opt/boost_1_59_0/include -c++ -python  example.i 
mpicxx -c example.cpp  example_wrap.cxx -I /opt/local/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/numpy/core/include  -I /opt/Eigen3/include/eigen3 -I /opt/boost_1_59_0/include -I/opt/Eigen3/include/eigen3/unsupported
#mpicxx -shared example.o example_wrap.o -L/opt/local/lib -L /opt/boost_1_59_0/lib -L /opt/ALPSCore/lib -lpython2.7 -lboost_system -lalps-gf -lalps-hdf5 -lalps-utilities -o _example.so 
mpicxx -shared example.o example_wrap.o -L/opt/local/lib  -lpython2.7  -o _example.so 
