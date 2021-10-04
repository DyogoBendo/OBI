// Guilherme A. Pinto, OBI-2018, cinco

#include <bits/stdc++.h>
using namespace std;

vector<int> digito;
int N;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  
  cin >> N;
  digito = vector<int>(N);

  for( int i = 0; i < N; i++ )
    cin >> digito[i];

  int ze = -1; // zero mais a esquerda
  int cd = -1; // cinco mais a direita
  int zce = -1; // zero ou cinco, mais a esquerda

  for( int i = 0; i < N; i++ ){
    if ( digito[i] == 0 and ze == -1 ) ze = i;
    if ( digito[i] == 5 ) cd = i;
    if ( (digito[i] == 5 or digito[i] == 0) and zce == -1 ) zce = i; 
  }

  // nenhum digito 0, nem digito 5
  if ( zce == -1 ){
    cout << -1 << endl;
    return 0;
  }
  
  if ( digito[N-1] < 5 ){ // digito da unidade: 1, 2, 3 ou 4
    if ( ze != -1 ){
      swap( digito[ze], digito[N-1] );
    } else {
      swap( digito[cd], digito[N-1] );
    }
  } else { // digito da unidade: 6, 7, 8 ou 9
    swap( digito[zce], digito[N-1] );
  }

  for( int i = 0; i < N; i++ ){
    cout << digito[i];
    if ( i < N-1 ) cout << " ";
  }
  cout << endl;
  
  return 0;
}
