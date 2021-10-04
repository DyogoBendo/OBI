// Guilherme A. Pinto, OBI-2017, mapa

#include <iostream>

#define MAX 105

using namespace std;

string m[MAX],buf;
int d[5] = {0,-1,0,1,0};

int main(){
  int L,C,l,c,a,b;
  
  cin >> L >> C;

  m[0] = string(C+2,'.');
  for ( int i = 1; i <= L; i++ ){
    cin >> buf;
    m[i] = "." + buf + ".";
  }
  m[L+1] = string(C+2,'.');

  for ( int i = 1; i <= L; i++ )
    for ( int j = 1; j <= C; j++ )
      if ( m[i][j] == 'o' ) { l = i; c = j; }

  bool moveu = true;
  while ( moveu ){
    moveu = false;
    for ( int k = 0; k < 4; k++ ){
      a = l+d[k]; b = c+d[k+1];
      if ( m[a][b] == 'H' ){
	m[l][c] = '.';
	l = a; c = b;
	moveu = true;
	break;
      }
    }
  }
  
  cout << l << " " << c << endl;
			   
  return 0;
}
