#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>


using namespace std;

int N;
vector<int> adj[1<<20];
// essa bfs guardará 2 valores, quanto ao peso acumulado e a posicao 
// atual 
queue<pair<int,int> > bfs;
int marked[1<<20];

int main(){
	scanf("%d", &N);
	for(int i = 0; i < N-1; i++){
		int a,b;
		scanf("%d %d", &a, &b);
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	bfs.push(make_pair(0,1));
	int menor = -1, idx = -1;
	while(!bfs.empty()){
		int val = bfs.front().first;
		int ii = bfs.front().second;
		bfs.pop();
		if(marked[ii])continue;
		marked[ii] = 1;
		if(menor < val){
			menor = val;
			idx = ii;
		}
		for(int i = 0; i < adj[ii].size(); i++){
			if(!marked[adj[ii][i]])
				bfs.push(make_pair(val+1, adj[ii][i]));
		}
	}
	menor = -1;
	memset(marked,0,sizeof marked);
	bfs.push(make_pair(0,idx));
	while(!bfs.empty()){
		int val = bfs.front().first, ii = bfs.front().second;
		bfs.pop();
		if(marked[ii])continue;
		marked[ii] = 1;
		if(menor < val){
			menor = val;
			idx = ii;
		}
		for(int i = 0; i < adj[ii].size(); i++){
			if(!marked[adj[ii][i]])
				bfs.push(make_pair(val+1, adj[ii][i]));
		}
	}
	printf("%d\n", menor);
	return 0;
}

