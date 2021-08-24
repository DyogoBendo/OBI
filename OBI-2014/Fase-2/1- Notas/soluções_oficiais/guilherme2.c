/* Guilherme A. Pinto, OBI 2014, notas */

#include <stdio.h>

#define MIN 0
#define MAX 100

#define MAXN 200

int notas[MAXN];

int main(){
  int N,i,j,count,max,maxnota;

  /* leitura dos dados */
  scanf("%d",&N);
  for ( i = 0; i < N; i++ )
    scanf("%d",&notas[i]);
  
  max = 0; maxnota = 0;
  for ( i = 0; i <= MAX; i++ ){
    count = 0;
    for ( j = 0; j < N; j++ )
      if ( notas[j] == i ) count++;
    if ( count >= max ){
      max = count;
      maxnota = i;
    }
  }

  printf("%d\n", maxnota);

  return 0;
}
