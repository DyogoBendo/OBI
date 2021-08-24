#include <iostream>
using namespace std;

int main(){
  int N,D,A;
  
  cin >> N >> D >> A;

  int vezes = 0;
  
  while( A != D ){
    A++;
    if ( A > N ) A = 1;
    vezes++;    
  }

  cout << vezes << endl;
  
  return 0;
}
