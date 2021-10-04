// OBI-2019, detetive, Guilherme A. Pinto

#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

int E, I, V, A, B, X;
int stamp, flag;
vector<vector<int>> implica, implicado, consequencia;
vector<int> verdadeiro, m, res, nec;
queue<int> q;

// intersecao de dois vetores ordenados (intersecao de conjuntos)
vector<int> intersecao( const vector<int>& A, const vector<int>& B ){
  vector<int> I;

  int a = 0;
  int b = 0;
  while( a < A.size() and b < B.size() )
    if ( A[a] == B[b] ){
      I.push_back( A[a] );
      a++; b++;
    } else {
      if ( A[a] < B[b] ) a++;
      else b++;
    }

  return I;
}

void dfs( int e, vector<int>& nec ){
  if ( m[e] == stamp ) return;
  m[e] = stamp;

  if ( implicado[e].empty() ){ // evento sem causa
    if ( flag ){
      flag = false;
      nec = consequencia[e];
    } else {
      nec = intersecao( nec, consequencia[e] );
    }
    return;
  }
  
  for( int c: implicado[e] ) // para cada possivel causa
    dfs( c, nec );
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  
  cin >> E >> I >> V;
  
  implica = vector<vector<int>>(E+1);
  implicado = vector<vector<int>>(E+1);
  consequencia = vector<vector<int>>(E+1);
  m = vector<int>(E+1,0);
  res = vector<int>(E+1,0);

  // entrada
  for ( int i = 0; i < I; i++ ){
    cin >> A >> B;
    implica[A].push_back( B );   // A implica B
    implicado[B].push_back( A ); // B implicado por A
  }
  
  for ( int i = 0; i < V; i++ ){
    cin >> X;
    verdadeiro.push_back( X );
  }
  
  stamp = 0;

  // computa conjunto de consequencias de cada evento sem causa
  for ( int i = 1; i <= E; i++ )
    if ( implicado[i].empty() ){

      // BFS
      m[i] = ++stamp;
      q.push( i );
      consequencia[i].push_back( i );
      while( not q.empty() ){
        int k = q.front(); q.pop();
        for ( int j: implica[k] )
          if ( m[j] < stamp ){
            m[j] = stamp;
            q.push( j );
            consequencia[i].push_back( j );
          }
      }
      sort(consequencia[i].begin(), consequencia[i].end());
    }

  // para cada evento 'e' verdadeiro da entrada, computa a interseção
  // dos conjuntos de consequências de todos os eventos sem causa
  // que têm 'e' como consequência
  for ( int e: verdadeiro ){
    nec = vector<int>();
    stamp++; flag = true;

    // DFS
    dfs( e, nec );

    for ( int k: nec )
      res[k] = 1;
  }

  // saida
  string sep = "";
  for ( int i = 1; i <= E; i++ )
    if ( res[i] ){
      cout << sep << i;
      sep = " ";
    }
  cout << endl;
  
  return 0;
}
