#include <stdio.h>

#define MAX_N (1123)
int degree[MAX_N];

int main(){
  int m, n, i, x, y, v, res, soma = 0;
  char c;
  scanf("%d %d", &m, &n);
  for (i = 1; i <= n; ++i)
      degree[i] = 0;
  for (i = 0; i < m; ++i) {
    scanf("%d %d %d", &x, &v, &y);
    degree[x] += v;
    degree[y] -= v;
    soma += v;
  }
  res = 0;
  for (i = 1; i <= n; ++i) 
    if (degree[i] > 0) res += degree[i];
  if (res < soma) c = 'S';
  else c = 'N';
  printf("%c\n%d\n", c, res);
  return 0;
}
