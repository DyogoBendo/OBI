// Guilherme A. Pinto, soma, O(N), OBI-2019

#include <bits/stdc++.h>

#define MAX 500000

typedef long long ll;

using namespace std;

ll o[MAX],q[MAX+1],z[MAX+1];

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N,K;
  cin >> N >> K;

  for( int i = 0; i < N; i++ ) cin >> o[i];

  // remove zeros do vetor original o[] e cria vetor auxiliar z[]
  // contendo o numero de zeros a esquerda de cada nao-zero
  //
  // entrada, o[]: 2 0 1 1 0 0 8 4 1 3, produz:
  //
  //          q[]: 2 1 1 8 4 1 3
  //          z[]: 0 1 0 2 0 0 0 0
    
  int cnt = 0, k = 0;
  
  for( int i = 0; i < N; i++ )
    if ( o[i] == 0 ) cnt++;
    else {
      q[k] = o[i];
      z[k++] = cnt;
      cnt = 0;
    }

  z[k] = cnt;
  N = k;
  q[N] = 0; // sentinela
  
  ll count = 0LL;
  
  if ( K == 0 ){

    // sequencia de z[i] zeros possui combinacao de z[i]+1, 2 a 2, retangulos
    for( int i = 0; i <= N; i++ ) count += ((z[i]+1)*z[i])/2;    

  } else {

    // dois ponteiros sobre o vetor de nao-zeros
    int l = 0, r = 0; 
    int soma = q[0]; 
    
    while( r < N ){
      if ( soma <= K ){
	if ( soma == K ) count += (z[l]+1)*(z[r+1]+1);
	soma += q[++r]; // move ponteiro direito
      } else {
	soma -= q[l++]; // move ponteiro esquerdo
	if ( l > r ){
	  r = l;
	  soma = q[r]; // reinicia janela
	}
      }
    }
    
  }  

  cout << count << endl;
  
  return 0;
}
