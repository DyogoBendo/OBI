// Guilherme A. Pinto, idade, OBI-2019

#include <stdio.h>

int main(){

  int M, A, B; // idade de d. Monica e dois de seus filhos
  int C;       // idade do outro filho
  int res;     // idade do filho mais velho

  scanf("%d%d%d", &M, &A, &B);
  
  C = M-A-B;

  res = A;
  if ( res < B ) res = B;
  if ( res < C ) res = C;

  printf("%d\n", res);
  
  return 0;
}
