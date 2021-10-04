// Guilherme A. Pinto, chuva, dfs, OBI-2019

#include <bits/stdc++.h>

#define MAX 500

using namespace std;

int N,M;
string w[MAX];

void dfs( int i, int j ){
  // molha
  w[i][j] = 'o';

  // base
  if ( i == N-1 ) return;

  // recursao
  if ( w[i+1][j] == '.' ) dfs( i+1, j );
  if ( w[i+1][j] == '#' ){
    if ( w[i][j-1] == '.' ) dfs( i, j-1 );
    if ( w[i][j+1] == '.' ) dfs( i, j+1 );
  }
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> N >> M;

  for( int i = 0; i < N; i++ )
    cin >> w[i];

  dfs( 0, w[0].find('o') );

  for( int i = 0; i < N; i++ )
    cout << w[i] << endl;
  
  return 0;
}
