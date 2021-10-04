#include <stdio.h>

int n;

int main(void) {
  int i,x,troca=0,repara=0;

  scanf("%d",&n);
  for (i=0;i<n;i++) {
    scanf("%d",&x);
    if (x<50)
      troca++;
    else if (x<85)
      repara++;
  }
  printf("%d %d\n",troca,repara);
}
