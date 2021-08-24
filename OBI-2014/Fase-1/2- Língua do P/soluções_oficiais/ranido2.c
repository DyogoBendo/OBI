#include<stdio.h>
#include<strings.h>

#define MAX 1000

char codigo[MAX+2];
char mensagem[MAX];
int i, m, size;

int main(void) {
  m=0;
  while (scanf("%s",codigo)==1) {
    if (m!=0)
	mensagem[m++]=' ';
    size=strlen(codigo);
    for (i=0; i<size; i++)
      mensagem[m++]=codigo[++i];
  }
  printf("%s\n", mensagem);
  return 0;
}
