#include <iostream>
#include <cstdio>
#include <algorithm>

#define MAXN 1000

using namespace std;

int max_food, now_food;
char field[MAXN][MAXN];

void visit(char cell) {
  if (cell == 'A') now_food = 0;
  else if (cell == 'o') now_food++;
  max_food = max(max_food, now_food);
}

int main() {
  int n;

  scanf("%d", &n);

  for (int y = 0; y < n; y++)
    for (int x = 0; x < n; x++)
      scanf(" %c", &field[y][x]);

  max_food = 0, now_food = 0;
  for (int y = 0; y < n; y++)      
    if (y%2 == 0) {
      for (int x = 0; x < n; x++)
	visit(field[y][x]);
    } else {
      for (int x = n-1; x >= 0; x--)
	visit(field[y][x]);
    }

  printf("%d\n", max_food);

  return 0;
}
