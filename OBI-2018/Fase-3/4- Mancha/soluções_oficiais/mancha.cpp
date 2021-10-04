// Guilherme A. Pinto, mancha, OBI-2018

#include <bits/stdc++.h>

using namespace std;

// irregular se e somente se uma linha ou coluna contem
// o padrao:  dentro -> fora -> dentro


int N;
vector<string> m;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  
  cin >> N;

  for( int i = 0; i < N; i++ ){
    string aux;
    cin >> aux;
    m.push_back(aux);
  }

  char res = 'S';
  bool done = false;
  
  // linhas
  for( int i = 0; i < N and not done; i++ ){
    int p = 0;
    for( int j = 0; j < N and not done; j++ ){
      if ( m[i][j] == '*' and (p == 0 or p == 2) ) p++;
      if ( m[i][j] == '.' and (p == 1)) p++;
      if ( p == 3 ){
	res = 'N';
	done = true;
      }
    }
  }

  // colunas
  for( int j = 0; j < N and not done; j++ ){
    int p = 0;
    for( int i = 0; i < N and not done; i++ ){
      if ( m[i][j] == '*' and (p == 0 or p == 2) ) p++;
      if ( m[i][j] == '.' and (p == 1)) p++;
      if ( p == 3 ){
	res = 'N';
	done = true;
      }
    }
  }

  cout << res << endl;
  
  return 0;
}
