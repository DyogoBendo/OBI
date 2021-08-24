/* Guilherme A. Pinto, OBI 2014, blefe */

#include <stdio.h>
#include <stdlib.h>

#define MAXN 1000
#define MAXM 10000

int N,M;
int A[MAXN],B[MAXM];

int comp(const void * a, const void * b){
  return ( *(int*)a - *(int*)b );
}

int soma( i ){
  int k,l,val,sum;
  val = B[i];

  k = 0; l = i-1;
  while( k <= l ){
    sum = B[k]+B[l]; 
    if ( sum == val ) return 1;
    else { 
      if ( sum > val ) l--;
      else k++; 
    }
  }
  return 0;
}

int main(){
  int i,j,yes,aux;
  int *ret;

  scanf("%d%d",&N,&M);

  for( i = 0; i < N; i++ ) scanf("%d",&A[i]);
  for( i = 0; i < M; i++ ) scanf("%d",&B[i]);

  qsort( A, N, sizeof(int), comp );

  for( yes = 1, i = 0; i < M; i++ ){
    /* procura em A */
    ret = bsearch( &B[i], A, N, sizeof(int), comp );
    if ( ret == NULL )
      if ( !soma( i ) ){
	yes = 0;
	break;
      }
    /* insertion sort */
    for ( j = i-1; j >= 0; j-- )
      if ( B[j] > B[j+1] ){
	aux = B[j]; B[j] = B[j+1]; B[j+1] = aux;
      }
  }

  if ( yes ) printf("sim\n");
  else printf("%d\n",B[i]);

  return 0;
}
