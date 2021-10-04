#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
bitset<N> a[N];
bitset<N> ans[N];
vector<int> radj[N];
int in[N] , out[N] , dg[N];
bool ist[N] , source[N];
vector<int> verdadeiro;
vector<int> adj[N];
int e , I , V;
bool vis[N];

void dfs(int x){
	ist[x] = true;
	vis[x] = true;
	for(auto w : radj[x]){
		if(!vis[w]){
			dfs(w);		
		}
	}
}

int32_t main(){
	scanf("%d%d%d" , &e , &I , &V);
	for(int i = 1 ; i <= e; i ++){
		a[i][i] = true;
	}
	for(int i = 0 ; i < I ; i ++){
		int x , y;
		scanf("%d%d" , &x , &y);
		adj[y].push_back(x);
		radj[x].push_back(y);
		out[x]++ , in[y]++;
		dg[x]++;
	}
	for(int i = 0 ; i < N ; i ++){
		for(int j = 0 ; j < N ; j ++){
			ans[i][j] = true;
		}
	}
	for(int i = 1 ; i <= V; i ++){
		int x;
		scanf("%d" , &x);
		ist[x] = true;
		verdadeiro.push_back(x);
	}
	queue<int> q;
	for(int i = 1 ; i <= e ;i ++){
		if(in[i] == 0){
			source[i] = true;
		}
		if(out[i] == 0){
			q.push(i);
		}
	}
	while(!q.empty()){
		int u = q.front();
		q.pop();
		for(auto w : adj[u]){
			a[w] |= a[u];
			dg[w]--;
			if(dg[w] == 0) q.push(w);
		}
	}
	for(int i = 1 ; i <= e ;i ++){
		if(source[i]){
			for(int j = 1 ; j <= e; j ++){
				if(a[i][j] && ist[j]){
					ans[j] &= a[i];
				}
			}
		}
	}
	for(auto w : verdadeiro){
		for(int j = 1 ; j <= e ;j ++){
			if(ans[w][j]){
				ist[j] = true;
			}
		}
	}
	for(int i = 1 ; i <= e ;i ++){
		if(!vis[i] && ist[i]){
			dfs(i);
		}
	}
	bool last = false;
	for(int i = 1 ; i <= e; i ++){
		if(ist[i]){
			if(last){
				printf(" ");
			}
			last = 1;
			printf("%d" , i);
		}
	}
	printf("\n");
}
