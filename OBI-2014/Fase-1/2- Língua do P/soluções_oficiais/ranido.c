#include<stdio.h>
#include<strings.h>

#define MAX 1000

char codigo[MAX+2];
char mensagem[MAX];
int i, m, size;

int main(void) {
  gets(codigo);
  size=strlen(codigo);
  m=0;
  for (i=0; i<size; i++) {
    if (codigo[i]==' ')
      mensagem[m++]=' ';
    else {
      i++;
      mensagem[m++]=codigo[i];
    }
  }
  printf("%s\n", mensagem);
  return 0;
}
