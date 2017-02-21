#include "example.hpp"

//double My_variable = 3.0;

//int fact(int n) {
           //if (n <= 1) return 1;
                //else return n*fact(n-1);
                 //}
 
//int my_mod(int x, int y) {
          //return (x%y);
           //}
    //
 //char *get_time()
     ////{
              //time_t ltime;
                   //time(&ltime);
                        //return ctime(&ltime);
                         //}

double rms(double* seq, int n) {
    double sum = 0.0;
    for (int i = 0; i < n; ++i) {
        sum += seq[i];
    }
    return sum;
}
