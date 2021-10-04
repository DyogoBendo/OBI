// Guilherme A. Pinto, bolas, OBI-2018

#include <bits/stdc++.h>
using namespace std;

int b[9];

int main(){
  bool sim = false;
  
  for( int i = 0; i < 8; i++ )
    cin >> b[i];

  // menor permutacao (lexicografica)
  sort( b, b+8 );

  do {
    bool viz = false;
    // checa se permutacao tem vizinhas iguais
    for ( int i = 0; i < 7; i++ )
      if ( b[i] == b[i+1] )
	viz = true;
    // se achou permutacao sem vizinhas iguais, para
    if ( not viz ){
      sim = true;
      break;
    }
  } while( next_permutation( b, b+8 ) );
  
  if ( sim ) cout << "S" << endl;
  else cout << "N" << endl;

  return 0;
}
