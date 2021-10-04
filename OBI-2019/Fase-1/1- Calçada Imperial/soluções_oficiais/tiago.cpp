#include <bits/stdc++.h>
using namespace std;

int32_t main(){
	int ans = 1;
	int n;
	cin>>n;
	vector<int> v(n);
	for(int i = 0 ; i < n; i ++) cin>>v[i];
	for(int i = 0 ; i < n; i ++){
		for(int j = 0 ; j < n; j ++){
			int curr = 0;
			int last = -1;
			for(int k = 0 ; k < n ;k ++){
				if((v[k] == v[i] || v[k] == v[j]) && v[k] != last){
					curr++;
					last = v[k];
				}
			}
			ans = max(ans ,curr);
		}
	}
	cout<<ans<<endl;
}