// r. anido
// problema xerxes, OBI2017

#include <stdio.h>

int n;                 // número de partidas
int d,x;               // apostas de dario e xerxes
int nd=0,nx=0;         // número total de partidas ganhas por dario e xerxes

int main (void) {
  int i;

  scanf("%d", &n);         // lê número de partidas
  for (i=0; i<n; i++) {
    scanf("%d%d", &d, &x); // lê as duas apostas
    if (x==0)
      x = 5;
    if (d<x) {
      if ((x-d)<=2)
	nd++;              // dario ganha a partida
      else
	nx++;              // xerxes ganha a partida
    }
    else if ((d-x)<=2)
	nx++;              // xerxes ganha a partida
      else
	nd++;              // dario ganha a partida
  }
  if (nd>nx)
	printf("dario\n");   // dario ganha o jogo
  else
	printf("xerxes\n");   // xerxes ganha o jogo

  return 0;
}
