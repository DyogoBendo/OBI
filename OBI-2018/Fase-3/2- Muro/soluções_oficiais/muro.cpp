// Guilherme A. Pinto, muro, OBI-2018

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define MAXN 10000
#define MOD 1000000007LL

int N;
ll muro[MAXN+1];

int main(){

  cin >> N;

  // base
  muro[0] = 1LL;
  muro[1] = 1LL;
  muro[2] = 5LL;

  // recursao
  for ( int i = 3; i <= N; i++ )
    muro[i] = (muro[i-1]+4*muro[i-2]+2*muro[i-3])%MOD;

  cout << muro[N] << endl;

  return 0;
}
