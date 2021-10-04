// rede social
// obi2020 - fase 3

#include <iostream>
#include <algorithm>
using namespace std;

int comp(int const &i, int const &j) {
  return i > j;
}

int main(void) {
  int n, x;
  
  cin >> n;
  int repostagens[n];

  for (int i=0; i < n; i++)
    cin >> repostagens[i];

  int rep_size = sizeof(repostagens) / sizeof(repostagens[0]);
  // ordena do maior para o menor
  sort(repostagens, repostagens + rep_size, comp);

  int fi = 0;
  while (fi < n && repostagens[fi] >= fi + 1)
    fi++;

  cout << fi << endl;

}
