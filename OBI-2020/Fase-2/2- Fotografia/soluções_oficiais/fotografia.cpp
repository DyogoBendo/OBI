// OBI2020 - Fase 2
// fotografia

#include <cstdio>
using namespace std;

int foto[2];
int moldura[2];

int main(void) {
  int n, x, y;
  int melhor_moldura = -1;
  int menor_area = 200 * 200;

  scanf("%d%d", &x, &y);
  if (x > y) {
    foto[0] = y; foto[1] = x;
  }
  else {
    foto[0] = x; foto[1] = y;
  }
  
  scanf("%d", &n);
  int area = foto[0] * foto[1];
  for (int i=0; i<n; i++) {
    scanf("%d%d", &x, &y);
    if (x > y) {
      moldura[0] = y; moldura[1] = x;
    }
    else {
      moldura[0] = x; moldura[1] = y;
    }
    if (moldura[0] >= foto[0] && moldura[1] >= foto[1]) {
      // moldura serve
      if (moldura[0] * moldura[1] - area < menor_area) {
	melhor_moldura = i+1;
	menor_area = moldura[0] * moldura[1] - area;
      }
    }
  }
  printf("%d\n", melhor_moldura);

  return 0;
}


