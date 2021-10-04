#include <bits/stdc++.h>
using namespace std;
const int N = 4*(200505);
vector<int> adj[N];
int idx[N];
int ridx[N];
bool vis[N];
int n;
bool dfsTree[N];

int aux = 0;
void build(int l , int r , int curr = 1){
	int mid = (l+r)/2;
	if(l == r){
		idx[curr] = l;
		ridx[l] = curr;
		return ;
	}
	idx[curr] = n + (++aux);
	build(l,mid,2*curr);
	build(mid +1 , r, 2*curr + 1); 
	adj[idx[curr]].push_back(idx[2*curr]);
	adj[idx[curr]].push_back(idx[2*curr +1]);

}

struct node{
	int u , L , R;
}; 

vector<node> v;
int m , l , r, ansj = -2;

void create(int i , int x , int y , int l = 1 , int r = n , int curr = 1){
	int mid = (l+r)/2;
	if(l == x && r == y){
		adj[i].push_back(idx[curr]);
		return ;
	}
	if(y <= mid){
		create(i , x, y, l ,mid , 2*curr);
	}
	else if(x > mid){
		create(i , x, y, mid + 1 , r, 2*curr +1);
	}
	else{
		create(i , x, mid ,l , mid, 2*curr);
		create(i , mid + 1, y,  mid + 1 ,r , 2*curr + 1);
	}
}

bool dfs(int x){
	vis[x] = true;
	dfsTree[x] = true;
	bool p = false;
	for(auto w : adj[x]){
		if(vis[w] && dfsTree[w]){
			return 1;
		}
		else if(!vis[w]){
			p |= dfs(w);
		}
	}
	dfsTree[x] = false;
	return p;
}



int32_t main(){
	scanf("%d%d" , &n , &m);
	v.resize(m);
	for(int i = 0 ; i <m ; i ++) scanf("%d%d%d" , &v[i].u , &v[i].L , &v[i].R);
	l = 0, r = m - 1;
	while(l<=r){
		for(int i = 0 ; i <= 4*(n + 400) ; i++){
			adj[i].clear();
			vis[i] = false;
			dfsTree[i] = false;
		}	
		aux = 0;	
		build(1 , n);
		int mid = (l+r)/2;
		for(int i = 0 ; i <= mid ; i ++){

			create(v[i].u , v[i].L , v[i].R);
		}
		bool ans = false;
		for(int i = 1 ; i <= n; i ++){
			if(!vis[i] && !ans){
				ans |= dfs(i);
			}
		}
		if(ans){
			ansj = mid;
			r = mid - 1;
		}
		else{
			l = mid + 1;
		}
	}
	printf("%d\n" , ansj + 1);
}
