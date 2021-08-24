#include <iostream>
#include <cstdio>

#define MAXN 500
#define MAXM 500

using namespace std;

int matrix[MAXN][MAXM];
bool acczero[MAXN][MAXM];

int main() {
  int n, m;

  scanf("%d %d", &n, &m);

  for (int y = 0; y < n; y++)
    for (int x = 0; x < m; x++)
      scanf("%d", &matrix[y][x]);

  for (int y = 0; y < n; y++)
    acczero[y][0] = (matrix[y][0] == 0);
  for (int x = 0; x < m; x++)
    acczero[n-1][x] = (matrix[n-1][x] == 0);
  for (int y = n-2; y >= 0; y--)
    for (int x = 1; x < m; x++)
      acczero[y][x] = (matrix[y][x] == 0 && acczero[y+1][x] && acczero[y][x-1]);

  bool ok = true;

  for (int y = 0; y < n; y++) {
    int first_non_zero = m;

    for (int x = 0; x < m; x++)
      if (matrix[y][x] != 0) {
	first_non_zero = x;
	break;
      }

    if (first_non_zero == m) {
      if (y+1 < n && !acczero[y+1][m-1]) ok = false;
    } else {
      if (y+1 < n && !acczero[y+1][first_non_zero]) ok = false;
    }
  }
  
  printf(ok ? "S\n" : "N\n");

  return 0;
}
