#include <stdio.h>
#include <stdlib.h>

#define MAX_N (112345)

#define min(x,y) ((x < y) ? x : y)

int compar(const void *m, const void *n) {
  return -(*((int *) m) - *((int *) n));
}

int v[MAX_N];

int main(int argc, char *noargs[]) {
  int i, j, n, k, res;
  scanf("%d %d", &n, &k);
  for (i = 0; i < n; ++i) scanf("%d", &v[i]);
  qsort(v, n, sizeof(int), compar);
  res = v[0] - v[n-1];
  for (i = 0; i <= k; ++i) {
    j = n -k + i - 1;
    if (i >= j) break;
    res = min(res, v[i] - v[j]);
    /* printf("%d %d %d %d %d %d\n", i, v[i], j, v[j], v[i]-v[j], res); */
  }
  printf ("%d\n", res);
}

