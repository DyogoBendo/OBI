/* Guilherme A. Pinto, OBI-2015, Caixinha */

#include <stdio.h>

typedef long long i64;

int N,M;

i64 min(i64 a, i64 b){ return (a<b)?a:b; };
i64 max(i64 a, i64 b){ return (a>b)?a:b; };

int main(){
  i64 res;
  int r;

  scanf("%d %d", &N, &M);

  res = 0;
  for( r = 1; r <= M; r++ )
    res += max(0, min(M, N-r-1)-max(1, N-r-M)+1);
  
  printf("%lld\n",res);

  return 0;
}
