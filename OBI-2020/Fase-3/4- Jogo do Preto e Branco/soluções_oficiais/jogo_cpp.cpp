#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
using namespace std;

int const MAX = 10;
int L, C, P;
int board[MAX][MAX];
set<pair<int, int>> possiveis;

int fill(int board[MAX][MAX], int i) {
  if (i >= possiveis.size())
    return 0;

  set<pair<int, int>>::iterator iter = possiveis.begin();
  advance(iter, i);
  int lin = (*iter).first;
  int col = (*iter).second;
  int brancas1 = 0, brancas2 = 0;
  if (board[lin][col] == 0) {
    // continua sem colocar peca branca
    brancas1 = fill(board,i+1);
    // continua colocando peca branca
    if (board[lin-1][col] != -1 and board[lin][col-1] != -1 and board[lin+1][col] != -1 and board[lin][col+1] != -1) {
      board[lin][col] = -1; // peca branca
      brancas2 = 1 + fill(board,i+1);
      board[lin][col] = 0; // restaura
    }
  }
  return max(brancas1,brancas2);
}

int main(void) {
  int max_num = 0;
  
  cin >> L >> C;

  // constroi tabuleiro com bordas de valor 2 para facilitar
  memset(board, 0, sizeof(board));
  for (int i = 0; i < L+2; i++) {
    board[i][0] = 2;
    board[i][C+1] = 2;
  }
  for (int j = 0; j < C+2; j++) {
    board[0][j] = 2;
    board[L+1][j] = 2;
  }

  cin >> P;

  // coloca pretas no tabuleiro e armazena vetor de pretas
  vector<pair<int,int>> pretas;
  for (int i = 0; i < P; i++) {
    int x, y;
    cin >> x >> y;
    board[x][y] = 1;  
    pretas.push_back(make_pair(x,y));
  }

  //constroi lista de possiveis
  for (auto const &p : pretas ) {
    int i = p.first, j = p.second;
    if (board[i+1][j] == 0)
      possiveis.insert(make_pair(i+1,j));
    if (board[i-1][j] == 0)
      possiveis.insert(make_pair(i-1,j));
    if (board[i][j+1] == 0)
      possiveis.insert(make_pair(i,j+1));
    if (board[i][j-1] == 0)
      possiveis.insert(make_pair(i,j-1));
  }

  //processa possíveis
  max_num = fill(board,0);
  cout << max_num << endl;
  
  return 0;
}      
