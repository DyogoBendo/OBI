// Guilherme A. Pinto, OBI-2017, arranhaceu

#include <iostream>

#define MAX 100000

using namespace std;

int bit[MAX+1], moradores[MAX+1];
int N;

void update(int x, int v) {
  while (x <= N){
    bit[x] += v;
    x += x&-x;
  }
}

int query(int x) {
  int r = 0;
  while( x ){
    r += bit[x];
    x -= x&-x;
  }
  return r;
}

int main()
{
  ios::sync_with_stdio(0);

  int Q,i;
  cin >> N >> Q;

  for ( i = 1; i <= N; i++ ){
    cin >> moradores[i];
    update( i, moradores[i] );
  }
  
  while ( Q-- > 0 ){
    int e,m,k;

    cin >> e;
    if ( e == 0 ){
      cin >> i >> m;
      int d = m - moradores[i];
      moradores[i] = m;
      update( i, d );
    } else {
      cin >> k;
      cout << query(k) << endl;
    }

  }
  
  return 0;
}
