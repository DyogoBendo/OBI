// Guilherme A. Pinto, OBI-2017, xerxes

#include <iostream>

using namespace std;

int main(){
  int N,D,X,nD;
  
  cin >> N;

  nD = 0;
  for ( int i = 0; i < N; i++ ){
    cin >> D >> X;
    if ( (X == (D+1)%5) || (X == (D+2)%5) ) nD++;
  }
  
  if ( nD > (N-nD) ) cout << "dario" << endl;
  else cout <<  "xerxes" << endl;
  
  return 0;
}
