// Guilherme A. Pinto, OBI-2019, mesa

#include <iostream>

using namespace std;

int c[3] = {0,0,0};
int A,B;

int main(){

  cin >> A >> B;

  // Ana
  int a = 1;
  while ( --A > 0 ) {
    a++;
    if ( a == 3 )
      a = 0;
  }

  c[a] = 1;

  // Beatriz
  int b = 1;
  while ( --B > 0 ) {
    b++;
    if ( b == 3 )
      b = 0;
  }

  // Mesma cadeira!
  if ( b == a ) {
    b++;
    if ( b == 3 ) 
      b = 0;
  }

  c[b] = 1;

  for ( int i = 0; i < 3; i++ )
    if ( c[i] == 0 ) // Cadeira onde Carolina vai sentar
      cout << i << endl;

  return 0;
}