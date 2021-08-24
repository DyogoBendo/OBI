#include <iostream>
#include <string>

using namespace std;

string d[1001], p[101];
int t[22][6], n, m;

int testa (string& a, string& b) {
  int sa = a.size(), sb = b.size();
  for (int i = 0; i <= 2; i++) t[0][i+2] = i;

  for (int i = 1; i <= sa; i++) {
    for (int j = -2; j <= 2; j++) {
      if (i+j < 0 && i+j > sb) continue;
      if (i+j == 0) {
        t[i][j+2] = i;
        continue;
      }
      
      if (a[i-1] == b[i+j-1]) t[i][j+2] = t[i-1][j+2];
      else {
        t[i][j+2] = t[i-1][j+2]+1;
        if (j != 2) t[i][j+2] = min(t[i][j+2], t[i-1][j+3]+1);
        if (j != -2) t[i][j+2] = min(t[i][j+2], t[i][j+1]+1);
      }
    }
  }
  
  int m = 10;
  for (int i = -2; i <= 2; i++) {
    if (sa + i < 0 || sa + i > sb) continue;
    m <?= t[sa][i+2] + sb - sa - i;
  }
  return (m < 3);
}

int main () {

  cin >> n >> m;
  
  for (int i = 0; i < n; i++) cin >> d[i];
  for (int j = 0; j < m; j++) cin >> p[j];
  
  for (int j = 0; j < m; j++) {
    for (int i = 0; i < n; i++) {
      if (testa(d[i], p[j]))
        cout << d[i] << " ";
    }
    cout << endl;
  }

  return 0;
}
