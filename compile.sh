swig -c++ -python example.i 
mpicxx-openmpi-clang38 -c example.cpp  example_wrap.cxx -I /opt/local/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/numpy/core/include -I /opt/ALPSCore/include -I /opt/boost_1_59_0/include #-L /opt/boost_1_59_0/lib
mpicxx-openmpi-clang38 -shared example.o example_wrap.o -L/opt/local/lib -L /opt/boost_1_59_0/lib -L /opt/ALPSCore/lib -lpython2.7 -lboost_system -lalps-gf -lalps-hdf5 -lalps-utilities -o _example.so 
