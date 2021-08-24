/* Guilherme A. Pinto, OBI-2015, Banco */

#include <stdio.h>

#define MAXS 5000

int n[7][MAXS+1];
int f[7][MAXS+1];
int m[7];
int v[7] = { -1, 2, 5, 10, 20, 50, 100 };

/**
 count(i,j): número de maneiras distintas de somar
 exatamente j, usando somente as notas disponíveis de
 valores v[1],v[2],...,v[i]
 */

int count( int k, int S ){
  int c;

  /* memoization */
  if ( f[k][S] ) return n[k][S];

  /* base da recursão */
  if ( S == 0 ) return 1; /* uma maneira: entregar nenhuma nota */
  if ( k == 0 ) return 0;

  /* c: quantas notas do valor v[k] */
  c = 0; n[k][S] = 0;
  while( c <= m[k] && S-c*v[k] >= 0 )
    n[k][S] += count( k - 1, S-(c++)*v[k] );

  f[k][S] = 1;
  return n[k][S];
}

int main(){
  int i,j,S;

  for ( i = 0; i < 7; i++ )
    for ( j = 0; j < MAXS+1; j++ )
      f[i][j] = n[i][j] = 0;

  scanf("%d",&S);
  for ( i = 1; i <= 6; i++ )
    scanf("%d",&m[i]);

  printf("%d\n", count( 6, S ) );
  
  return 0;
}
