// Guilherme A. Pinto, OBI 2017, postes

#include <iostream>
using namespace std;

int main(){
  int N;
  int substituidos = 0;
  int consertados = 0;
  
  cin >> N;
  for ( int i = 0; i < N; i++ ){
    int X;
    cin >> X;
    if ( X < 50 ) substituidos++;
    if ( 50 <= X && X < 85 ) consertados++;
  }
  
  cout << substituidos << " " << consertados << endl;
  return 0;
}
