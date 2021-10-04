// Guilherme A. Pinto, muro, OBI-2018

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define MAXN 10000
#define MOD 1000000007LL

int N;
vector<ll> m;

ll muro( int i ){

  // memoization
  if ( m[i] != -1LL ) return m[i];

  // base
  if ( i == 0 or i == 1 ) return m[i] = 1LL;
  if ( i == 2 ) return m[i] = 5LL;

  // recursao
  return m[i] = (muro(i-1)+4*muro(i-2)+2*muro(i-3))%MOD;
}

int main(){

  cin >> N;

  m = vector<ll>(N+1,-1LL);
    
  cout << muro( N ) << endl;

  return 0;
}
