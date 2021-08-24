#include <stdio.h>

int buracos[4][2] = {
  {1, 3},
  {2, 3},
  {2, 5},
  {5, 4},
};

typedef enum {False, True} Boolean;

Boolean eh_buraco (int x, int y) {
  int i;
  for (i = 0; i < 4; ++i) {
    if ((x == buracos[i][0]) && (y == buracos[i][1]))
      return True;
  }
  return False;
}

int main(int argc, char *noargs[]) {
  int i, m, res, N, pos[2] = {4,3};
  int moves[9][2] = {
    {0, 0},
    {1, 2},
    {2, 1},
    {2, -1},
    {1, -2},
    {-1, -2},
    {-2, -1},
    {-2, 1},
    {-1, 2},
  };
  scanf ("%d", &N);
  res = N;
  for (i = 0; i < N; ++i) {
    scanf("%d", &m);
    pos[0] += moves[m][0];
    pos[1] += moves[m][1];
    if (eh_buraco(pos[0], pos[1])) {
      res = i + 1;
      break;
    }
  }
  printf("%d\n", res);
  return 0;
}
  
