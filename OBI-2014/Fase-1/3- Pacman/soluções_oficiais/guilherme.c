/* Guilherme A. Pinto - OBI 2014 - Pacman */

#include <stdio.h>

#define MAXN 100

char s[MAXN*MAXN];

int main() {
  int i,j,N,ans,c = 0;
  char str[MAXN+1];

  scanf("%d",&N);
  for ( i = 0; i < N; i++ ){
    scanf("%s",str);
    for ( j = 0; j < N; j++ ){
      if ( !(i%2) ) s[c++] = str[j];
      else s[c++] = str[N-1-j];
    }
  }
  
  for ( c = 0, ans = 0, i = 0; i < N*N; i++ ){
    if ( s[i] == 'o' ) c++;
    if ( s[i] == 'A' ){
      if ( c > ans ) ans = c;
      c = 0;
    }
  }
  if ( c > ans ) ans = c;
  
  printf("%d\n",ans);
  
  return 0;
}
