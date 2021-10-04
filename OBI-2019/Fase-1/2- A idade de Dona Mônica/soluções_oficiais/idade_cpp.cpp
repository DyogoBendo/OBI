// Guilherme A. Pinto, idade, OBI-2019

#include <iostream>
using namespace std;

int main(){

  int M, A, B; // idade de d. Monica e dois de seus filhos
  int C;       // idade do outro filho
  int res;     // idade do filho mais velho
  
  cin >> M >> A >> B;
  
  C = M-A-B;

  res = max(C,max(A,B));
  
  cout << res << endl;
  
  return 0;
}
