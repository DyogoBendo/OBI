/* Guilherme A. Pinto, OBI 2014, notas */

#include <stdio.h>

#define MIN 0
#define MAX 100

#define MAXN 200

int notas[MAX+1];

int main(){
  int N,i,val,max,maxi;

  for ( i = 0; i <= MAX; i++ ) notas[i] = 0;

  /* leitura dos dados */
  scanf("%d",&N);
  for ( i = 0; i < N; i++ ){
    scanf("%d",&val);
    notas[val]++;
  }
  
  max = 0; maxi = 0;
  for ( i = 0; i <= MAX; i++ )
    if ( notas[i] >= max ){
      max = notas[i];
      maxi = i;
    }
  
  printf("%d\n", maxi);

  return 0;
}
