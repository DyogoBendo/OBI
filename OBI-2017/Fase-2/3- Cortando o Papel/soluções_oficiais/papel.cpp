#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 100000

using namespace std;

vector<pair<int,int>> A(MAX);
int b[MAX+2];

int main(){
  ios::sync_with_stdio(0);
  int i,a,N;
  
  cin >> N;
  b[0] = b[N+1] = 0;
  for( i = 1; i <= N; i++ ){
    b[i] = 1;
    cin >> a;
    A.push_back( make_pair(a,i) );
  }

  sort( A.begin(), A.end() );

  int last = 0;
  int max,nt;
  max = nt = 1;
  for ( auto e : A ){
    a = e.first; i = e.second;
    if ( a != last ) if ( nt > max ) max = nt;
    b[i] = 0;
    if ( b[i-1] && b[i+1] ) nt++;
    if ( !b[i-1] && !b[i+1] ) nt--;
  }
  
  cout << max+1 << endl;
  return 0;
}
