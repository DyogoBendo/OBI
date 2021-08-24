/* Guilherme A. Pinto, OBI-2015, coral */

#include <stdio.h>

int main(){
  int A,B,C,D;
  
  scanf("%d %d %d %d", &A, &B, &C, &D);

  if ( A == C || B == D ) printf("V\n");
  else printf("F\n");
  
  return 0;
}
