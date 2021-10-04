// Guilherme A. Pinto, OBI 2017, frete

#include <iostream>
#include <vector>
#include <queue>

#define pb push_back
#define mp make_pair

#define MAX 1001

using namespace std;

int frete[MAX];
bool marca[MAX];
vector<pair<int,int>> cidade[MAX];
priority_queue<pair<int,int>> q;

int main(){
  int N,M,A,B,C,f;
  
  cin >> N >> M;
  for ( int i = 0; i < M; i++ ){
    cin >> A >> B >> C;
    cidade[A].pb(mp(B,C));
    cidade[B].pb(mp(A,C));
  }
  for ( int i = 1; i <= N; i++ )
    marca[i] = false;

  // Dijkstra
  
  q.push( mp(0,1) ); // frete total 0, origem 1
  while ( not q.empty() ){
    auto p = q.top(); q.pop();
    f = -p.first;
    A = p.second;
    if ( not marca[A] ){
      frete[A] = f;
      marca[A] = true;
      for ( auto e : cidade[A] ){
	B = e.first;
        C = e.second;
	if  ( not marca[B] )
	  q.push( mp(-(f+C),B) );
      }
    }
  }
  
  cout << frete[N] << endl;
  return 0;
}
