// OBI-2019 - Fase 2
// Supermercado

#include <stdio.h>

int main(void){
  int n;
  int g;               // gramas em cada supermercado
  float p,preco_grama; // preco em cada supermercado e menor preco conhecido por grama do produto
  
  scanf("%d", &n);
  
  preco_grama = 1000.0*1000;
  for (int i=0; i<n; i++) {
    scanf("%f%d", &p, &g);
    if (p/g < preco_grama)
        preco_grama = p / g;
  }
  printf("%.2f\n",1000*preco_grama);
  
  return 0;
}
