#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#define MAX 1005

using namespace std;

struct ponto{
	int x, y;
	ponto(){}
	ponto(int _x, int _y){
		x = _x;
		y = _y;
	}
};

int dist1(const ponto &a, const ponto &b){
  return ((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

int dist(const ponto &a, const ponto &b){
  return floor(hypot(a.x-b.x, a.y-b.y));
}

//void printdist(const ponto &a, const ponto &b,int D){
//  printf("%f %f %d %d %d\n",floor(hypot(a.x-b.x, a.y-b.y)),hypot(a.x-b.x, a.y-b.y),(a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y),D,D*D);
//}

int N, D;
ponto arv[MAX];
vector <int> adj[MAX];
bool vis[MAX];

void dfs(int x){
	vis[x] = true;
	for (int i = 0; i < (int)adj[x].size(); i++)
		if (vis[adj[x][i]] == false)
			dfs(adj[x][i]);
}

int main(){
	scanf("%d%d", &N, &D);
	D=D*D;
	for (int i = 0; i < N; i++)
		scanf("%d%d", &arv[i].x, &arv[i].y);
	for (int i = 0; i < N; i++){
		vis[i] = false;
		adj[i].clear();
		for (int j = 0; j < N; j++){
			if (i == j)
				continue;
			if (dist1(arv[i], arv[j]) <= D)
				adj[i].push_back(j);				
			//if (dist1(arv[i], arv[j]) > D && dist(arv[i], arv[j]) <= D/D)
			//  printdist(arv[i], arv[j],D);

		}
	}
	dfs(0);
	bool flag = true;
	for (int i = 0; i < N; i++)
		if (vis[i] == false)
			flag = false;
	if (flag)
		printf("S\n");
	else
		printf("N\n");
	return 0;
}
