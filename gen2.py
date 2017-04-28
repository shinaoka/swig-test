for d in xrange(1,8):
    s = '''
  template<typename S, typename T> 
  struct copy_data_from_numpy_helper<%d,S,T> { 
    static void invoke(std::vector<int>& data_size, S* in, T* out) { 
      typedef CXXTypeTraits<T> traits; 
      const int dim = %d; 

      int lin_idx = 0; 
      std::vector<int> indices(dim);\n'''%(d,d)
    

    for i in xrange(d):
        s+= ' '*(6+2*i) + 'for (int i%d= 0; i%d< data_size[%d]; ++i%d) { '%(i,i,i,i) + '\n'
        s+= ' '*(6+2*i+2) + 'indices[%d] = i%d;'%(i,i) + '\n'
    
    s+=' '*(6+2*d)+'traits::element_at(*out, indices) = in[lin_idx];\n'
    s+=' '*(6+2*d)+'++lin_idx;\n'
    for i in xrange(d):
        s+= ' '*(6+2*d-2*i-2) + '}' + '\n'
    
    s+='''
    } 
  };
    '''
    
    print s
