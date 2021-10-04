// Guilherme A. Pinto, elevador, O(NlogN)

#include <bits/stdc++.h>
using namespace std;

vector<int> p;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N;
  
  cin >> N;
  p = vector<int>(N+1);

  // inclui sentinela
  p[0] = 0;
  
  for( int i = 1; i < N+1; i++ )
    cin >> p[i];

  sort(p.begin(), p.end());

  char res = 'S';
  
  for ( int i = 0; i < N; i++ )
    if ( p[i+1]-p[i] > 8 ){
      res = 'N';
      break;
    }

  cout << res << endl;
  
  return 0;
}
