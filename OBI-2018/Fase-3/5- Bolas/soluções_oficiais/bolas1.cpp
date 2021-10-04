// Guilherme A. Pinto, bolas, OBI-2018

#include <bits/stdc++.h>
using namespace std;

int contador[9];

int main(){
  int b;
  bool sim = true;
  
  for( int i = 0; i < 8; i++ ){
    cin >> b;
    contador[b]++;
    if ( contador[b] > 4 ) sim = false;
  }

  if ( sim ) cout << "S" << endl;
  else cout << "N" << endl;

  return 0;
}
