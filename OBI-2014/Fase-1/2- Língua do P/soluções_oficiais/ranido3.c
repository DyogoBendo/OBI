#include<stdio.h>
#include<strings.h>

#define MAX 1000

char codigo[MAX+2];
char mensagem[MAX];
int i, m, size, c;

int main(void) {
  m=0;
  while ((c=getchar())!='\n') {
    if (c==' ')
      mensagem[m++]=' ';
    else
      mensagem[m++]=getchar();
  }
  printf("%s\n", mensagem);
  return 0;
}
