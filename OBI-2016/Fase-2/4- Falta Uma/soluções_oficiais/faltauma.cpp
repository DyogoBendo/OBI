// Guilherme A. Pinto, 2016

#include <iostream>
using namespace std;

int count[9][9] = {};
int fat[9] = {1,1,2,6,24,120,720,5040,40320};

int main(){
  ios::sync_with_stdio(0);
  int N,d,p;
  
  cin >> N;
  for( int i = 1; i <= fat[N]-1; i++ )
    for( p = 1; p <= N; p++ ){
      cin >> d;
      count[p][d]++;
    }

  for( p = 1; p <= N; p++ ){
    if ( p > 1 ) cout << " ";
    for( d = 1; d <= N; d++ )
      if ( count[p][d] != fat[N-1] ){
	cout << d;
	break;
      }
  }
  cout << endl;

  return 0;
}
