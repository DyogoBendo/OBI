#include <stdio.h>

#define MAX_N (1123)
int adj[MAX_N][MAX_N];

#define min(x,y) (x <= y? x : y)

void dump(int n) {
  int i, j;
  for (i = 1; i <= n; ++i) {
    for (j = 1; j <= n; ++ j) {
      printf("%2d ", adj[i][j]);
    }
    printf("\n");
  }
}
  
int main(){
  int m, n, i, j, k, u, v, w, d, res, soma = 0;
  char c;
  scanf("%d %d", &m, &n);
  for (i = 1; i <= n; ++i)
    for (j = 1; j <= n; ++j)
      adj[i][j] = 0;
  for (k = 0; k < m; ++k) {
    scanf("%d %d %d", &i, &v, &j);
    adj[i][j] += v;
    soma += v;
  }
  /* dump(n); */
  for (v = 1; v <=n; ++v) {
    u = w = 1;
    while ((u <= n) && (w <= n)) {
      if (adj[u][v] == 0) {
	++u;
	continue;
      }
      if (adj[v][w] == 0) {
	++w;
	continue;
      }
      d = min(adj[u][v], adj[v][w]);
      if (u != w) adj[u][w] += d;
      adj[u][v] -= d;
      adj[v][w] -= d;
      /* printf("\nu = %d v = %d w = %d\n", u, v, w); */
      /* dump(n); */
    }
  }
  res = 0;
  for (v = 1; v <= n; ++v)
    for (w = 1; w <= n; ++w)
      res += adj[v][w];
  if (res < soma) c = 'S';
  else c = 'N';
  printf("%c\n%d\n", c, res);
  return 0;
}
