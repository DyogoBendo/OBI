#include <stdio.h>
#include <stdlib.h>

#define sqr(x) ((x)*(x))

typedef struct{
  int pai;
  int size;
} Noh;

typedef struct {
  int x;
  int y;
} Ponto;

Noh noh[1123];
Ponto ponto[1123];

int find (int i) {
  if (noh[i].pai != i)  noh[i].pai = find(noh[i].pai);
  return noh[i].pai;
}

int main(int argc, char *noargs[]) {
  int n, d, i, j, d2, comp;
  char res;
  scanf("%d %d", &n, &d);
  d2 = d * d;
  comp = n;
  for (i = 0; i < n; ++i) {
    scanf("%d %d", &ponto[i].x, &ponto[i].y);
    noh[i].pai = i;
    noh[i].size = 1;
  }
  for (i = 0; i < n; ++i) {
    for (j = 0; j < i; ++j) {
      if (sqr(ponto[i].x - ponto[j].x) + sqr(ponto[i].y-ponto[j].y) <= d2) {
	int fi = find(i), fj = find(j);
	if (fi != fj) {
	  comp--;
	  if (noh[fi].size <= noh[fj].size) {
	    noh[fi].pai = fj;
	    noh[fj].size += noh[fi].size;
	  }
	  else {
	    noh[fj].pai = fi;
	    noh[fi].size += noh[fj].size;
	  }
	}
      }
    }
  }
  if (comp == 1) res = 'S';
  else res = 'N';
  printf("%c\n", res);
  return 0;
}
