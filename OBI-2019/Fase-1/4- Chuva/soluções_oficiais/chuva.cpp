// Guilherme A. Pinto, chuva, simulacao direta O(NM), OBI-2019

#include <bits/stdc++.h>

#define MAX 500

using namespace std;

string w[MAX];

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N,M;
  cin >> N >> M;

  for( int i = 0; i < N; i++ )
    cin >> w[i];
  
  for( int i = 0; i < N; i++ ){
    if ( i > 0 ) {
      for( int j = 0; j < M; j++ )
	// de cima para baixo
	if ( w[i][j] == '.' and w[i-1][j] == 'o' )
	  w[i][j] = 'o';
    }
    if ( i < N-1 ) {
      for( int j = M-2; j >= 0; j-- )
	// para a esquerda
	if ( w[i][j] == '.' and w[i][j+1] == 'o' and
	     w[i+1][j+1] == '#' )
	  w[i][j] = 'o';
      for( int j = 1; j < M; j++ )
	// para a direita
	if ( w[i][j] == '.' and w[i][j-1] == 'o' and
	     w[i+1][j-1] == '#' )
	  w[i][j] = 'o';
    }
  }
  
  for( int i = 0; i < N; i++ )
    cout << w[i] << endl;
  
  return 0;
}
