#include <stdio.h>

#define MAX_N (11234)

#define max(x,y) (x >= y ? x : y)

typedef struct {
  int father;
  int depth;
} Person;

Person p[MAX_N + 1];

int num_depth[MAX_N + 1];
int num_present[MAX_N + 1];

void find_depth(int v) {
  if ((p[v].depth == 0) && (v != 0)) {
    find_depth(p[v].father);
    p[v].depth = 1 + p[p[v].father].depth;
  }
}

int main (int argc, char *noargs[]) {
  int n, m, i, v, max_depth = 0;
  char *sep = "";
  Person new = {0, 0};

  scanf("%d %d", &n, &m);

  for (i = 1; i <= m; ++i) num_depth[i] = num_present[i] = 0;

  p[0] = new;
  for (v = 1; v <= n; ++v) {
    p[v] = new;
    scanf("%d", &p[v].father);
  }
  for (v = 1; v <= n; ++v) {
    find_depth(v);
    ++num_depth[p[v].depth];
    max_depth = max(max_depth, p[v].depth);
  }
  for (i = 0; i < m; ++i) {
    scanf("%d", &v);
    ++num_present[p[v].depth];
  }

  for (i = 1; i <= max_depth; ++i) {
    printf("%s%2.2f", sep, 100.0 * num_present[i] / num_depth[i]); 
    sep = " ";
  }
  printf("\n");
  return 0;
}
