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
//namespace alps{
//double B::do_job() {return 0.0;}
//}

//double rms(double* seq, int n) {
//double rms(std::vector<double>& seq, int n) {
double drms(const std::vector<double>& seq) {
    int n = seq.size();
    double sum = 0.0;
    for (int i = 0; i < n; ++i) {
        sum += seq[i];
    }
    return sum;
}

dcomplex crms(const std::vector<dcomplex>& seq) {
    int n = seq.size();
    dcomplex sum = 0.0;
    for (int i = 0; i < n; ++i) {
        sum += seq[i];
    }
    return sum;
}

/*
std::complex<double> crms(std::complex<double>& seq, int n) {
    std::complex<double> sum = 0.0;
    for (int i = 0; i < n; ++i) {
        sum += seq[i];
    }
    return sum;
}
*/
