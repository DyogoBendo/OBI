#include <cstdio>
#include <cstring>
#include <utility>
#include <algorithm>

using namespace std;

#define ROW 0
#define COL 1

#define MAXR 50
#define MAXN 100000

int bit[3][MAXR + 2][MAXN + 2];

void add(int idx, int r, int pos, int valor) {

  for (int i = pos; i < MAXN; i += (i&-i))
    bit[idx][r][i] += valor;
}

int get(int idx, int r, int pos) {

  int soma = 0;
  for (int i = pos; i > 0; i -= (i&-i))
    soma += bit[idx][r][i];
  
  return soma;
}

pair < int, int > lastRow[MAXN + 1];
pair < int, int > lastCol[MAXN + 1];
int n,q;

int getBest(pair < int, int > lastV, int time_now, int IS_COL) {

  int soma = 0;
  int best_count = -1, best_save = -1;
  int lastR = lastV.first;
  int lastIdx = lastV.second;
  for (int R = 0; R <= 50; R++) {
    if (R == lastR) continue;
    int cur = get(IS_COL, R, time_now) - get(IS_COL, R, lastIdx);
    soma += cur;
    if (cur >= best_count) {
      best_count = cur;
      best_save = R;
    }
  }
  if (n - soma > best_count)
    best_save = lastR;
  else if(n - soma == best_count)
    best_save = max(best_save, lastR);

  return best_save;
}

int main() {

  scanf("%d %d", &n, &q);
  memset(bit, 0, sizeof(bit));
  for (int i = 0; i <= n; i++)
    lastRow[i] = lastCol[i] = make_pair(0,0);

  for (int t = 1; t <= q; t++) {
    int opr, x, R;
    scanf("%d %d", &opr, &x);
    
    switch (opr) {
    case 1:
      scanf("%d", &R);
      if (lastRow[x].second) 
	add(COL, lastRow[x].first, lastRow[x].second, -1);
      
      add(COL, R, t, 1);
      lastRow[x] = make_pair(R, t);
      break;
    case 2:
      scanf("%d", &R);
      if (lastCol[x].second)
	add(ROW, lastCol[x].first, lastCol[x].second, -1);
      add(ROW, R, t, 1);
      lastCol[x] = make_pair(R, t);
      break;
    case 3:
      printf("%d\n", getBest(lastRow[x], t, ROW));
      break;
    case 4:
      printf("%d\n", getBest(lastCol[x], t, COL));
      break;
    }

  }
  return 0;
}
