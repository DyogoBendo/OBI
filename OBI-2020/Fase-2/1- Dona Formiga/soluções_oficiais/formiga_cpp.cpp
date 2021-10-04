#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

const int MAX = 200;

int S, T, P;
int altura[MAX];
int visitado[MAX];
vector<int> adj[MAX];
int alcancados = 0;

void busca(int k) {
  if (!visitado[k]) {
    alcancados++;
    visitado[k] = 1;
    for (auto q : adj[k]) {
	busca(q);
    }
  }
}

int main(void) {
  int i, a, b;
  
  scanf("%d%d%d", &S, &T, &P);
  for (i=0; i<S; i++)
    scanf("%d", &altura[i]);

  for (i=0; i<T; i++) {
    scanf("%d%d", &a, &b);
    a--; b--;
    if (altura[a] > altura[b])
      adj[a].push_back(b);
    else if (altura[a] < altura[b])
      adj[b].push_back(a);
  }

  memset(visitado, 0, sizeof(visitado));
  busca(P-1);
  printf("%d\n", alcancados-1);
  
  return 0;
}
