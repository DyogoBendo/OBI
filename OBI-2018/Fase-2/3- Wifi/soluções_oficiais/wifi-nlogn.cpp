// Guilherme A. Pinto, wifi, O(NlogN)

#include <bits/stdc++.h>
using namespace std;

struct Event {
  int x, h1, h2;
  bool operator < ( const Event& o ) const {
    if ( x != o.x ) return x < o.x;
    return h1 < o.h1;
  }
};

vector<Event> e;

int N;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  
  cin >> N;
  for( int i = 0; i < N; i++ ){
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    // inclui eventos
    e.push_back({x1,y2,y1});
    e.push_back({x2,y2,y1});    
  }

  sort(e.begin(), e.end());

  int res = 0;

  // sweep line
  map<int,int> sl;

  // insere sala externa (primeiro evento apos sort)
  sl[e[0].h2] = 1;
  sl[e[0].h1] = 0;
  
  for ( int i = 1; i < e.size(); i++ ){

    auto it = sl.find( e[i].h1 );
    if ( it != sl.end() ){
      if ( it->second == 0 ) res++; // se sala estava vazia
      // remove sala
      sl.erase( it, next( it, 2 ) );
    } else {
      it = sl.lower_bound( e[i].h1 );
      --it;
      it->second = 1;
      // insere nova sala
      sl[e[i].h2] = 1;      
      sl[e[i].h1] = 0;
    }
    
  }
  
  cout << res << endl;
  
  return 0;
}
