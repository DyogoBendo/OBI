// Guilherme A. Pinto, OBI 2017, imperio

#include <iostream>
#include <vector>

#define MAX 100001

using namespace std;

vector<int> g[MAX];
int N, C, res;

int dfs( int i, int pai ){
  int peso = 1;

  for ( auto p: g[i] )
    if ( p != pai )
      peso += dfs( p, i );
  
  int dif = abs(N-2*peso);
  if ( dif < res ) res = dif;
  
  return peso;
}

int main(){
  int A,B;
  
  cin >> N;
  for ( int i = 1; i <= N-1; i++ ){
    cin >> A >> B;
    g[A].push_back(B);
    g[B].push_back(A);
  }
  
  res = N;
  dfs( 1, -1 );
  
  cout << res << endl;
  return 0;
}
