// trem da mina
// obi2020 - fase 3

#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

#define INF 1000000000
#define NON_VISITED -1 
#define VISITED 1

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

vi dist;
vi curdist;
vector<vii> AdjList;
int C, T, Q, mindist,wormlen;
vi dfs_num;

void dijkstra(int start) {
  priority_queue< ii, vector<ii>, greater<ii> > pq; 
  pq.push(ii(0, start));
  dist.assign(C, INF);
  dist[start] = 0;
  while (!pq.empty()) {
    ii front = pq.top(); pq.pop();
    int d = front.first, u = front.second;
    if (d > dist[u]) continue;
    for (int j = 0; j < (int)AdjList[u].size(); j++) {
      ii v = AdjList[u][j];   
      if (dist[u] + v.second < dist[v.first]) {
	dist[v.first] = dist[u] + v.second;
	pq.push(ii(dist[v.first], v.first));
      } 
    } 
  }
}

void dfs(int u, int c, int from) {
  int lencycle;

  dfs_num[u] = VISITED;      // visited
  curdist[u]=c;
  for (int j = 0; j < (int)AdjList[u].size(); j++) {
    ii v = AdjList[u][j];
    if (v.first == from) continue;
    if (dfs_num[v.first] == NON_VISITED)
      dfs(v.first,c+v.second,u);
    else { // found cycle
      //printf("v.first=%d,v.second=%d,   %d+%d=%d %d\n ",v.first+1,v.second,c,v.second,curdist[v.first],dist[v.first]);
      //printf("len=%d+%d=%d\n ",c+v.second-curdist[v.first],2*dist[v.first],c+v.second-curdist[v.first]+2*dist[v.first]);
      lencycle=c+v.second-curdist[v.first];
      if (lencycle>=wormlen && mindist>lencycle+2*dist[v.first])
	mindist=lencycle+2*dist[v.first];
    }
  } 
}

int main() {
  int a, b, w, start;

  scanf("%d %d", &C, &T);

  AdjList.assign(C, vii());
  for (int i = 0; i < T; i++) {
    scanf("%d %d %d", &a, &b, &w);
    a--; b--;
    AdjList[a].push_back(ii(b, w));
    AdjList[b].push_back(ii(a, w));
  }
  scanf("%d", &Q);
  for (int i=0; i<Q; i++) {
    scanf("%d %d", &start, &wormlen);
    start--;
    dijkstra(start);
    dfs_num.assign(C, NON_VISITED);
    mindist=INF;
    curdist.assign(C, INF);
    dfs(start,0,-1);
    if (mindist==INF)
      mindist=-1;
    printf("%d\n",mindist);

  }
  return 0;
}
