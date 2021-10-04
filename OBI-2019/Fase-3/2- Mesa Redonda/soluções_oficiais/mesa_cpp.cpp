// Guilherme A. Pinto, OBI-2019, mesa

#include <iostream>

using namespace std;

int c[3] = {0,0,0};
int A,B;

int main(){

  cin >> A >> B;

  // Ana
  c[A%3] = 1;

  // Beatriz
  if ( c[B%3] == 1 ) {
    c[(B+1)%3] = 1;
  } else {
    c[B%3] = 1;
  }

  for ( int i = 0; i < 3; i++ )
    if ( c[i] == 0 )
      cout << i << endl;

  return 0;
}