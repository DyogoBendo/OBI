/* Guilherme A. Pinto - OBI 2014 - Copa */

#include <stdio.h>
#include <stdlib.h>

typedef struct _edge { int p,q,w; } edge;

#define MAXN 101  /* max number of points + 1 */
#define MAXW 1000 /* max weight */
#define W(v) (v<1001)?v:v-MAXW

int comp(const void * a, const void * b){ 
  return (((edge*)a)->w)-(((edge*)b)->w);
}

edge e[2*MAXN*MAXN];
int set[MAXN];
int N,F,R;

void makeset( int a ){ set[a] = a; }
int  find( int a ){ return set[a]; }
void unite( int a, int b ){
  int i, bs = set[b], as = set[a];
  for ( i = 1; i <= N; i++ ) 
    if ( set[i] == bs ) 
      set[i] = as;
}

int main() {
  int i,j,p,q,w,ans;

  scanf("%d%d%d",&N,&F,&R);
  for ( i = 0; i < F+R; i++ ){
    scanf("%d%d%d",&p,&q,&w);
    e[i].p = p; e[i].q = q;
    if ( i < F ) e[i].w = w;
    else e[i].w = w + MAXW;
  }

  /* kruskal */
  qsort( e, i, sizeof(edge), comp );
  for ( i = 1; i <= N; i++ ) makeset( i );
  ans = i = j = 0;
  while( j < N-1  ) {
    p = e[i].p; q = e[i].q;
    if ( find( p ) != find( q ) ){
      ans += W(e[i].w); 
      unite( p, q );
      j++;
    }
    i++;
  }

  printf("%d\n",ans);
  return 0;
}
