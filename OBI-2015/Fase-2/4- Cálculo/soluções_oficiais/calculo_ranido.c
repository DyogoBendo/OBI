/*
  r. anido
  tarefa Calculo, OBI2015, Fase 2
*/

#include <stdio.h>
#include <assert.h>

#define MAX 1000

int x[MAX],y[MAX],res[MAX];

int main(void) {
  int m,n,i,max_mn,vaium,r;

  // lê entrada
  scanf("%d%d",&m,&n);
  max_mn=m>n?m:n;
  for (i=0; i<m; i++)
    scanf("%d", &x[i]);
  for (i=0; i<n; i++)
    scanf("%d", &y[i]);

  // faz x e y terem o mesmo número de dígitos
  for (i=m; i<max_mn; i++)
    x[i]=0;
  for (i=n; i<max_mn; i++)
    y[i]=0;

  // calcula o resultado
  vaium=0;
  for(i=max_mn-1; i>=0; i--) {
    r=x[i]+y[i]+vaium;
    if (r<=1)
      vaium=0;
    else
      vaium=1;
    res[i]=r%2;
  }
  assert(vaium==0);

  // elimina zeros do final
  while (res[max_mn-1]==0)
    max_mn--;
  // imprime resultado
  for (i=0; i<max_mn-1; i++) {
    printf("%d ", res[i]);
  }
  printf("%d\n", res[max_mn-1]);
  return 0;
}
