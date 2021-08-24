/* Guilherme A. Pinto - OBI 2014 - Lingua */

#include <stdio.h>
#include <stdlib.h>

#define MAXN 1002

char code[MAXN];
char msg[MAXN];

int main() {
  char c;
  int i, p;
  
  i = 0; p = 0;
  while ( (c = getchar()) != '\n' )
    if ( c != ' ' ){
      if ( p == 0 ) p = 1;
      else {
	msg[i++] = c;
	p = 0;
      }
    } else msg[i++] = ' ';
  
  msg[i] = '\0';
  
  printf("%s\n",msg);
  return 0;
}
