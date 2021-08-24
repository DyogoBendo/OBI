#include <iostream>
#include <cstdio>
#include <vector>

#define MAXN 100000

typedef long long lint;

using namespace std;

vector<int> adj[MAXN];
bool mark[MAXN];
int many;

void dfs(int v) {
  many++;
  mark[v] = true;

  for (int i = 0; i < (int)adj[v].size(); i++) {
    int v2 = adj[v][i];
    if (!mark[v2])
      dfs(v2);
  }
}

int main() {
  int n;
  cin >> n;

  for (int i = 0; i < n-1; i++) {
    int a, b, c;
    cin >> a >> b >> c; a--, b--;
    if (c == 0) {
      adj[a].push_back(b);
      adj[b].push_back(a);
    }
  }

  for (int i = 0; i < n; i++) mark[i] = false;

  lint result = (lint)n * (n-1) / 2;

  for (int i = 0; i < n; i++)
    if (!mark[i]) {
      many = 0;
      dfs(i);
      result -= (lint)many * (many-1) / 2;
    }

  cout << result << endl;

  return 0;
}
