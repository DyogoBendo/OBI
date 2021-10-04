// OBI2020
// dona formiga

#include <stdio.h>
#include <string.h>

#define TAM 200

int S, T, P, altura[TAM], visitado[TAM];
char adj[TAM][TAM];
int alcancados = 0;

void busca(int k) {
  int q, tmp;
  
  if (visitado[k] == -1) {
    alcancados++;
    visitado[k] = 0;
    for (q = 0; q < S; q++) {
      if (adj[k][q])
	busca(q);
    }
  }
}

int main(void) {
  int i, a, b;
  
  scanf("%d%d%d", &S, &T, &P);
  for (i=0; i<S; i++)
    scanf("%d", &altura[i]);
  memset(adj, 0, sizeof(adj));
  for (i=0; i<T; i++) {
    scanf("%d%d", &a, &b);
    a--; b--;
    if (altura[a] > altura[b])
      adj[a][b] = 1;
    else if (altura[a] < altura[b])
      adj[b][a] = 1;
  }
  memset(visitado, -1, sizeof(visitado));
  busca(P-1);
  printf("%d\n", alcancados-1);
  
  return 0;
}
