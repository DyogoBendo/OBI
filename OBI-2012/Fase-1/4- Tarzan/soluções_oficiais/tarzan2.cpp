#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

ll X[1010], Y[1010], N, D;
#define sq(x) ((x)*(x))
vector<int> adj[1010];
int marked[1010];
void dfs(int idx){
	if(marked[idx])return;
	marked[idx] = 1;
	for(int i = 0; i < adj[idx].size(); i++)dfs(adj[idx][i]);
}
int main(){
	cin >> N >> D;
	D *= D;
	for(int i = 0; i < N; i++)cin >> X[i] >> Y[i];
	for(int i = 0; i < N; i++){
		for(int j = i+1; j < N; j++){
			if(sq(X[i]-X[j])+sq(Y[i]-Y[j]) <= D){
				adj[i].push_back(j);
				adj[j].push_back(i);
			}
		}
	}
	memset(marked,0,sizeof marked);
	dfs(0);
	int ok = 1;
	for(int i = 0; i < N && ok; ok &= marked[i++]);
	if(ok){
		cout << "S" << endl;
	}else{
		cout << "N" << endl;
	}
	return 0;
}
