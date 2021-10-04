// OBI-2019 - Fase 2
// Supermercado

#include <iostream>
#include <iomanip>
using namespace std;

int main(){

  int n;
  int g;               // gramas em cada supermercado
  float p,preco_grama; // preco em cada supermercado e menor preco conhecido por grama do produto
  
  cin >> n;

  preco_grama = 1000.0*1000;
  for (int i=0; i<n; i++) {
    cin >> p >> g;
    if (p/g < preco_grama)
        preco_grama = p / g;
  }
  cout.setf(ios::fixed);
  cout << setprecision(2) << 1000*preco_grama << endl;
  
  return 0;
}
