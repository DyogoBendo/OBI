// OBI-2019, metro, O(N+M), Guilherme A. Pinto

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> g[2]; // grafos Circulo e Quadrado
vector<int> d,pai;
queue<int> Q;
int c[2]; // vertice central
int N,M;

// BFS
int bfs( int i, const vector<vector<int>>& g ){
  d = vector<int>(g.size(),-1);
  pai = vector<int>(g.size(),-1);

  d[i] = 0;
  Q.push( i );

  int v;

  while( not Q.empty() ){
    v = Q.front(); Q.pop();
    for( int u: g[v] )
      if ( d[u] == -1 ){
        d[u] = d[v] + 1;
        pai[u] = v;
        Q.push( u );
      }
  }

  return v; // ultimo vertice a sair da fila
}

int main(){
  ios::sync_with_stdio(false); cin.tie(0);

  cin >> N >> M;

  g[0] = vector<vector<int>>(N+1);
  g[1] = vector<vector<int>>(M+1);

  for( int k: {0,1} )
    for( int i = 1; i <= g[k].size()-2; i++){
      int A,B;
      cin >> A >> B;
      g[k][A].push_back(B);
      g[k][B].push_back(A);
    }

  int l;

  for( int k: {0,1} ){
    // encontra um diametro no grafo
    l = bfs( bfs( 1, g[k] ), g[k] );

    // encontra o primeiro vertice central no diametro do grafo
    c[k] = l;
    while( d[c[k]] > d[l]/2 ) 
      c[k] = pai[c[k]];
  }
 
  cout << c[0] << " " << c[1] << endl;

  return 0;
}