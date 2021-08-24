#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

vector< vector<int> > child;
vector<bool> went;
vector<int> genmany, genwent;

void dfs(int v, int dist) {
  genmany[dist]++;
  if (went[v]) genwent[dist]++;
 
  for (int i = 0; i < (int)child[v].size(); i++) {
    int c = child[v][i];
    dfs(c, dist + 1);
  }
}

int main() {
  int n, m;

  scanf("%d %d", &n, &m);

  child = vector< vector<int> >(1+n);
  went = vector<bool>(1+n, false);

  for (int id = 1; id <= n; id++) {
    int p;
    scanf("%d", &p);
    child[p].push_back(id);
  }

  for (int i = 0; i < m; i++) {
    int id;
    scanf("%d", &id);
    went[id] = true;
  }
  
  genmany = vector<int>(1+n, 0);
  genwent = vector<int>(1+n, 0);

  dfs(0, 0);

  for (int d = 1; genmany[d] > 0; d++) {
    if (d-1 >= 1) printf(" ");
    printf("%.2f", 100.0 * genwent[d] / genmany[d]);
  }
  printf("\n");

  return 0;
}
