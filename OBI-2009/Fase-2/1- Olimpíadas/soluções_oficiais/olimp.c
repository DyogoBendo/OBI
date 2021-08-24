#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXN 112

int paises[MAXN];
int ouro[MAXN], prata[MAXN], bronze[MAXN];

int cmp(const void *ii, const void *jj) {
  int i = *((int *)ii), j = *((int *)jj);
  int o = ouro[i] - ouro[j], p = prata[i] - prata[j], b = bronze[i] - bronze[j];
  if (o > 0) return -1; if (o < 0) return 1;
  if (p > 0) return -1; if (p < 0) return 1;
  if (b > 0) return -1; if (b < 0) return 1;
  if (i < j) return -1; if (j > i) return 1;
  return 0;
}

int main() {
  int n, m;

  scanf("%d%d", &n, &m);

  memset(ouro, 0, sizeof(ouro));
  memset(prata, 0, sizeof(prata));
  memset(bronze, 0, sizeof(bronze));

  for (int i = 0; i < m; i++) {
    int o, p, b;
    scanf(" %d%d%d", &o, &p, &b);
    ouro[o-1]++; prata[p-1]++; bronze[b-1]++;
  }

  for (int i = 0; i < n; i++) paises[i] = i;
  qsort(paises, n, sizeof(paises[0]), cmp);
  printf("%d", paises[0]+1);
  for (int i = 1; i < n; i++)
    printf(" %d", paises[i]+1);
  printf("\n");

  return 0;
}
