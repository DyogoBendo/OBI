/* Chocolate - Felipe Abella */

#include <cstdio>

using namespace std;

int main() {
  int n;
  scanf("%d", &n);

  int x[2], y[2];
  for (int i = 0; i < 2; ++i)
    scanf("%d %d", &x[i], &y[i]), --x[i], --y[i];

  if ((x[0] < n/2) != (x[1] < n/2) ||
      (y[0] < n/2) != (y[1] < n/2))
    printf("S\n");
  else
    printf("N\n");

  return 0;
}
