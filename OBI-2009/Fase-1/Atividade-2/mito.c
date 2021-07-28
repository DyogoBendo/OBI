/* Solucao para o problema "Caçadores de Mito" da OBI 2009
   por: Igor Ribeiro de Assis */
#include <stdio.h>
#include <string.h> 		/* memset() */

#define MAXX 510
#define MAXY 510

/* para marcar onde cairam os raios */
int mapa[MAXX][MAXY];

int main() {
  int N, x, y, i;
  int caiu = 0;

  scanf("%d", &N);

  memset(mapa, 0, sizeof(mapa));
  for (i = 0; i < N; i++) {
    scanf("%d%d", &x, &y);
    /* se mapa[x][y] >= 1, entao já caiu um raio nesse quadrante */
    if (mapa[x][y]++)
      caiu = 1;
  }

  printf("%d\n", caiu);

  return 0;
}
