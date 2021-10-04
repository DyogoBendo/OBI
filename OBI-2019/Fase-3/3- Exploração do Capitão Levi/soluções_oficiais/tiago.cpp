#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define allin(a , x) for(auto a : x)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

template<class T1, class T2>
istream &operator>>(istream &in, pair<T1, T2> &P){
	in >> P.first >> P.second;
	return in;
}
template<class T1, class T2>
ostream &operator<<(ostream &out, const pair<T1, T2> &P){
	out << "(" << P.first << ", " << P.second << ")";
	return out;
}
template<class T>
istream &operator>>(istream &in, vector<T> &arr){
	for(auto &x: arr) in >> x;
	return in;
}
template<class T>
ostream &operator<<(ostream &out, const vector<T> &arr){
	for(auto &x: arr) out << x << ' '; cout << "\n";
	return out;
}
template<class T>
istream &operator>>(istream &in, deque<T> &arr){
	for(auto &x: arr) in >> x;
	return in;
}
template<class T>
ostream &operator<<(ostream &out, const deque<T> &arr){
	for(auto &x: arr) out << x << ' '; cout << "\n";
	return out;
}
const int N = 500005;

// ORDERED SET

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

// order_of_key
typedef tree<
pair<ll, int>,
null_type,
less<pair<ll, int>>,
rb_tree_tag,
tree_order_statistics_node_update> ordered_set; 
// END OF ORDERED SET
int n ;
ll p , q;
ordered_set Q;
int32_t main(){
	scanf("%d%lld%lld" ,&n,&p,&q);
	if(q < 0) p*=-1LL , q*=-1LL;
	ll ans = 0;
	vector<pair<ll,ll>> v(n);
	for(int i= 0;i<n;i++) scanf("%lld%lld" , &v[i].first,&v[i].second);
	sort(v.begin() , v.end());
	for(int i = 0 ; i < n ; i ++){
		ll x = v[i].first , y = v[i].second;
		ans += Q.order_of_key({q*y - p*x , (int) 1e9});
		Q.insert({q*y - p*x , i}); 
	}
	cout<<ans<<endl;
}