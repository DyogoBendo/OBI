// Guilherme A. Pinto, baldes, OBI-2018

#include <iostream>

using namespace std;

#define MAXN 100001

#define MAXV 1000000
#define MINV 1

#define MEIO(i,f) ((i)+(((f)-(i)+1)/2)-1)
#define ESQ(i) (2*(i))
#define DIR(i) (2*(i)+1)

#define MAX 131072 // 2^17

typedef pair<int,int> pii;

struct segment {
  int min_i, max_i; // indice do balde que contem o minimo (maximo) no segmento
  int i, f;
};

segment t[2*MAX+1]; // segment tree
int mi[MAXN+1],ma[MAXN+1]; // minimo (maximo) peso em cada balde
int N,M;

void init( int k, int i, int f ){
  t[k].i = i; t[k].f = f;
  t[k].min_i = t[k].max_i = 0; // aux
  if ( i > N ) return;
  if ( i != f ){
    init( ESQ(k), i, MEIO(i,f) );
    init( DIR(k), MEIO(i,f)+1, f );
  } else {
    mi[i] = MAXV+1;
    ma[i] = MINV-1;
    t[k].min_i = t[k].max_i = i;
  }
}

// point update: adicionar bola de peso p no balde b
void update( int k, int b, int p ){
  if ( t[k].i == t[k].f ){ // t[k].i == b
    mi[b] = min(mi[b],p);
    ma[b] = max(ma[b],p);
  } else {
    if ( b <= t[ESQ(k)].f ){ // ESQ
      update( ESQ(k), b, p );
      if ( mi[t[ESQ(k)].min_i] < mi[t[k].min_i] ) t[k].min_i = t[ESQ(k)].min_i;
      if ( ma[t[ESQ(k)].max_i] > ma[t[k].max_i] ) t[k].max_i = t[ESQ(k)].max_i;
    } else { // DIR
      update( DIR(k), b, p );
      if ( mi[t[DIR(k)].min_i] < mi[t[k].min_i] ) t[k].min_i = t[DIR(k)].min_i;
      if ( ma[t[DIR(k)].max_i] > ma[t[k].max_i] ) t[k].max_i = t[DIR(k)].max_i;
    }
  }
}

// range query: retorna o indice do balde que contem o minimo (maximo) no segmento [l,r]
pii query( int k, int l, int r ){
  
  // estritamente fora, sem recursao
  if ( t[k].i > r or t[k].f < l ) return {-1,-1};

  // estritamento dentro, sem recursao
  if ( t[k].i >= l and t[k].f <= r ) return {t[k].min_i,t[k].max_i};
  
  // recursao, nem dentro, nem fora
  pii e = query( ESQ(k), l, r );
  pii d = query( DIR(k), l, r );

  int min_i, max_i;
  min_i = max_i = 0; // aux
  
  if ( e.first != -1 and mi[e.first] < mi[min_i] ) min_i = e.first;
  if ( e.second != -1 and ma[e.second] > ma[max_i] ) max_i = e.second;
  if ( d.first != -1 and mi[d.first] < mi[min_i] ) min_i = d.first;
  if ( d.second != -1 and ma[d.second] > ma[max_i] ) max_i = d.second;
  
  return {min_i,max_i};
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  
  cin >> N >> M;

  int pw = 1; while( pw < N ) pw *= 2;

  // inicializa segtree e vetor de minimos e maximos por balde
  init( 1, 1, pw );
  // indice 0 eh auxiliar
  mi[0] = MAXV+1;
  ma[0] = MINV-1;
  //////////////////////
  
  for( int i = 1; i <= N; i++ ){
    int p;
    cin >> p;
    update( 1, i, p );
  }  
  
  for( int o = 0; o < M; o++ ){
    int t, a, b;
    cin >> t >> a >> b;
    if ( t == 1 ){
      update( 1, b, a );
    } else {
      pii s = query( 1, a, b );
      if ( s.first != s.second ){
	cout <<  abs(ma[s.second]-mi[s.first]) << endl;
      } else {
	pii e,d;
	int k = s.first;
	int res = -1;
	if ( k > a ){
	  e = query( 1, a, k-1 );
	  res = max(res,abs(ma[k]-mi[e.first]));
	  res = max(res,abs(ma[e.second]-mi[k]));
	}
	if ( k < b ){
	  d = query( 1, k+1, b );
	  res = max(res,abs(ma[k]-mi[d.first]));
	  res = max(res,abs(ma[d.second]-mi[k]));	  
	}
	cout << res << endl;
      }
    }
  }
  
  return 0;
}
