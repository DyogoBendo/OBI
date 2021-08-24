/* Calculo - Felipe Abella */

#include <algorithm>
#include <cstdio>

#define MAXS 1000

using namespace std;

int x[MAXS], y[MAXS], ret[MAXS];

int main() {
  int m, n;
  scanf("%d %d", &m, &n);

  for (int i = 0; i < m; ++i) scanf("%d", &x[i]);
  for (int i = 0; i < n; ++i) scanf("%d", &y[i]);

  int maxs = max(m, n);

  for (int i = maxs-1, c = 0; i >= 0; --i) {
    int v = x[i] + y[i] + c;
    ret[i] = v % 2;
    c = v / 2;
  }

  int s = 0;
  for (int i = 0; i < maxs; i++) if (ret[i]) s = i+1;

  for (int i = 0; i < s; i++) {
    if (i > 0) printf(" ");
    printf("%d", ret[i]);
  }
  printf("\n");

  return 0;
}
