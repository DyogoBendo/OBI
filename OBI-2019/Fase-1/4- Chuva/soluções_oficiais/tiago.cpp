#include <bits/stdc++.h>
using namespace std;

int32_t main(){
	int n , m ;
	cin>>n>>m;
	vector<string> v(n);
	for(int i = 0 ; i < n ;i ++) cin>>v[i];
	for(int i = 0 ; i < n; i ++){
		for(int j = 0 ; j < m; j ++){
			if(v[i][j] != '.') continue;
			if((i-1) >= 0 && v[i-1][j] == 'o') v[i][j] = 'o';
			if(((j-1) >= 0 && (i+1) < n && v[i][j-1] == 'o' && v[i+1][j-1] == '#') || ((j+1) <m && (i+1) < n && v[i][j+1] == 'o' && v[i+1][j+1] == '#')) v[i][j] = 'o';
		}
		for(int j = m-1 ; j >=0 ; j --){
			if(v[i][j] != '.') continue;
			if(((j-1) >= 0 && (i+1) < n && v[i][j-1] == 'o' && v[i+1][j-1] == '#') || ((j+1) <m && (i+1) < n && v[i][j+1] == 'o' && v[i+1][j+1] == '#')) v[i][j] = 'o';
		}
	}
	for(int i = 0 ; i < n; i ++){
		cout<<v[i]<<endl;
	}
}