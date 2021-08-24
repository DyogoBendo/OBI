/* Guilherme A. Pinto - OBI 2014 - Fechadura */

#include <stdio.h>
#include <stdlib.h>

#define MAXN 1000
int f[MAXN];

int main() {
  int i,N,M,ans = 0;
  
  scanf("%d%d",&N,&M);
  for ( i = 0; i < N; i++ ) 
    scanf("%d",&f[i]);
  
  i = 0;
  while( i < N-1 ){
    ans += abs(M-f[i]);
    if ( f[i] == f[i+1] ) i++;
    else f[i+1] += M-f[i];
    i++; 
  }
  
  printf("%d\n",ans);
  return 0;
}
