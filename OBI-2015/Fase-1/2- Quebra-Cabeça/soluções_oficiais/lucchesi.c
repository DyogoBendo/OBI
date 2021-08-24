#include <stdio.h>

#define MAX_N (112345)
#define MAX_D (212345)

int n;
int esq[MAX_D];
int dir[MAX_N];
char c[MAX_N];

int main(int argc, char *noargs[]) {
  int i, e;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%d %c %d", &e, &c[i], &dir[i]);
    esq[e] = i;
  }
  e = 0;
  for (i = 0; i < n; ++i) {
    printf("%c", c[esq[e]]);
    e = dir[esq[e]];
  }
  printf("\n");
  return 0;
}
