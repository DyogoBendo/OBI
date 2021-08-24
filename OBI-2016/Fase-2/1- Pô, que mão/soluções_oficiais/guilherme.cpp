// Guilherme A. Pinto, OBI-2016, po que mao

#include <bits/stdc++.h>

using namespace std;

int main() {
  int N,X,Y,Z;

  cin >> N >> X >> Y >> Z;

  int menor = min( X, min( Y, Z ) );
  int maior = max( X, max( Y, Z ) );
  int total = X + Y + Z;

  int res = 0;
  
  if ( N >= total ) {
    res = 3;
  } else {
    if ( N >= total - maior ) {
      res = 2;
    } else {
      if ( N >= menor )
	res = 1;
    }
  }
  
  cout << res << endl;
  
  return 0;
}
