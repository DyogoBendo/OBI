#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX 500
#define pega(i, j, k) ((k >= 0 && abs((i) - (j)) <= k) ? ((i >= 0 && j >= 0) ? tabela[i][j][k] : 0) : INT_MIN)

int n, num[2];
int linha[2][MAX];
int tabela[MAX][MAX][MAX];
int resposta;

int max(int a, int b, int c) {
  if (a > b)
    if (a > c) return a;
    else return c;
  else
    if (b > c) return b;
    else return c;
}

void processa() {
  int i, j, k, l, m;

  l = n * 2 - num[0] - num[1];
  if (l > num[0] + num[1]) l = num[0] + num[1];
  
  for (i = 0; i < num[0]; i++) {
    for (j = 0; j < num[1]; j++) {
	m = l - abs(num[0] - i - num[1] + j);
	for (k = abs(i - j); k <= m; k++)
	  tabela[i][j][k] = max(pega(i, j - 1, k - 1), pega(i - 1, j, k - 1), pega(i - 1, j - 1, k) + linha[0][i] * linha[1][j]);
    }
  }
  
  resposta = INT_MIN;
  for (k = abs(i - j); k <= l; k++) {
    if (resposta < tabela[num[0] - 1][num[1] - 1][k])
      resposta = tabela[num[0] - 1][num[1] - 1][k];
  }
}

int main(void) {
  int i;
  
  scanf("%d", &n);
  scanf("%d", &num[0]);
  for (i = 0; i < num[0]; i++)
    scanf("%d", &linha[0][i]);
  for (i = num[0]; i < n; i++)
    linha[0][i] = 0;
  scanf ("%d", &num[1]);
  for (i = 0; i < num[1]; i++)
    scanf ("%d", &linha[1][i]);
  for (i = num[1]; i < n; i++)
    linha[1][i] = 0;

  processa();

  printf ("%d\n", resposta);

  return 0;
}
