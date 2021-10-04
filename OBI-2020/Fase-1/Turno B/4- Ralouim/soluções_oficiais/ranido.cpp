#include<bits/stdc++.h> 
using namespace std;

typedef pair<int, int> pairs; 

vector<pair <int, pairs>> pares; 
vector<pairs> pontos;


int main(void) {
  int n, x, y;

  scanf("%d", &n);
  int melhor[n+1];
  int pmelhor[n+1];
  int pdist[n+1];

  pontos.push_back(make_pair(0,0));
  memset(melhor, 0, sizeof(melhor));
  memset(pmelhor, 0, sizeof(pmelhor));
  memset(pdist, 0, sizeof(pdist));

  for (int i=0; i<n; i++) {
    scanf("%d%d", &x, &y);
    pontos.push_back(make_pair(x,y));
  }
  for (int i=0; i<n+1; i++) {
    for (int k=i+1; k<n+1; k++) {
      int dx = pontos[i].first - pontos[k].first;
      int dy = pontos[i].second - pontos[k].second;
      pares.push_back(make_pair(dx*dx + dy*dy, make_pair(i,k)));
    }
  }

  sort(pares.begin(), pares.end());
  
  for (auto x : pares) {
    int d = x.first;
    int a = x.second.first;
    int b = x.second.second;
    
    if (d != pdist[a]) {
      pdist[a] = d;
      pmelhor[a] = melhor[a];
    }
    if (d != pdist[b]) {
      pdist[b] = d;
      pmelhor[b] = melhor[b];
    }
    if (a == 0)
      melhor[a] = max(melhor[a], pmelhor[b]);
    else {
      melhor[a] = max(melhor[a], 1+pmelhor[b]);
      melhor[b] = max(melhor[b], 1+pmelhor[a]);
    }
  }
  printf("%d\n",melhor[0]+1);
  return 0;
}
