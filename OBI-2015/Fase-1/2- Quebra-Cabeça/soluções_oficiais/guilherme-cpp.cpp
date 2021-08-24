/* Guilherme A. Pinto, OBI-2015, Quebracabeca */

#include <iostream>

#define MAXV 200000

using namespace std;

int direita[MAXV+1];
char letra[MAXV+1];

int main(){
  int N,E;

  cin >> N;
  
  for ( ; N > 0; N-- ){
    cin >> E;
    cin >> letra[E] >> direita[E];
  }
  
  for ( E = 0; E != 1; E = direita[E] )
    cout << letra[E];

  cout << endl;
  
  return 0;
}
