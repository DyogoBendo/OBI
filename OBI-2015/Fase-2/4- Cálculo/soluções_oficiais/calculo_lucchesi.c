/* OBI 2015 - Cláudio L. Lucchesi */

#include <stdio.h>

#define MAX_LEN (1123)

#define max(x,y) x >= y ? x : y

int X[MAX_LEN], Y[MAX_LEN];

int main(int argc, char *noargs[]) {
  int M, N, ell, i, carry;
  char *space;
  scanf ("%d %d", &M, &N);
  ell = max(M, N);
  for (i = 0; i < M; ++i) scanf("%d", &X[i]);
  for (i = 0; i < N; ++i) scanf("%d", &Y[i]);
  for (i = M; i < ell; ++i) X[i] = 0;
  for (i = N; i < ell; ++i) Y[i] = 0;
  carry = 0;
  for (i = ell - 1; i >= 0; --i) {
    X[i] += Y[i] + carry;
    if (X[i] < 2) {
      carry = 0;
    }
    else {
      carry = 1;
      X[i] -= 2;
    }
  }
  while (X[ell - 1] == 0) --ell;
  space = "";
  for (i = 0; i < ell; ++i) {
    printf("%s%d", space, X[i]);
    space = " ";
  }
  printf("\n");
  return 0;
}
