#include <stdio.h>

int freq[1123456];

int main(int argc, char *noargs[]) {
  int i, n, x, res = 0;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%d", &x);
    if (freq[x] == 0) {
      freq[x] = 1;
      res += 1;
    }
  }
  printf("%d\n", res);
  return 0;
}
