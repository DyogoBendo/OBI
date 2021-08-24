#include <stdio.h>

#define min(x,y) (x < y ? x : y)
#define max(x,y) (x > y ? x : y)

long long int f2(int n, int m) {
  int vmin, vmax;

  vmin = (n + 1) / 2;
  if (m < vmin) return 0;
  vmax = min(m, n - 1);
  return (vmax - vmin) * 2 + 1 + (n % 2);
}

int main(int argc, char *noargs[]) {
  int m, n;
  int v, vmin, vmax;
  long long int res;
  
  scanf("%d %d", &n, &m);
  res = 0;
  if (3 * m >= n + 2) {

    vmax = min(m, n - 1);
    vmin = max(1, n - 2 * vmax);
  
    fprintf(stderr, "vmin = %d vmax = %d\n", vmin, vmax);
    for (v = vmin; v <= vmax; ++v) {
      /* fprintf (stderr, "f2(%d, %d) = %d\n", n-v, m, f2(n-v, m)); */
      res += f2(n-v, m);
    }
  }

  printf ("%lld\n", res);
  return 0;
}
