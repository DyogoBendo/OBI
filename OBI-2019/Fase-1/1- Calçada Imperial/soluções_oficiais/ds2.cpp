// Guilherme A. Pinto, ds2, O(N^3), OBI-2019

#include <bits/stdc++.h>

#define MAX 501

using namespace std;

int V[MAX],N;

int maior( int a, int b, int pos ){
  // base
  if ( pos == N ) return 0;

  // recursao
  if ( V[pos] != a ) return maior( a, b, pos+1 );
  else return 1 + maior( b, a, pos+1 );
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> N;
  for( int i = 0; i < N; i++ ) cin >> V[i];

  int res = 1;
  for( int a = 1; a <= N; a++ )
    for( int b = 1; b <= N; b++ )
      if ( a != b )
	res = max( res, maior( a, b, 0 ) );
  
  cout << res << endl;
  
  return 0;
}
