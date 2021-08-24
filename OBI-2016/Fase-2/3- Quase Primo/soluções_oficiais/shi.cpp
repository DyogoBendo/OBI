#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

const int N = 41;
ll v[N];


int main (void) {
	ll n;
	int k;
	cin >> n >> k;
	for (int i = 0; i < k; ++i) {
		cin >> v[i];
	}	

	ll res = n;
	queue <tuple<ll, int,int>> q;
	q.push ( {1, -1, 0} );
	while (!q.empty()) {
		auto next = q.front(); q.pop();
		int p = get<1>(next);
		ll s = get<0>(next);
		int qt = get<2>(next);
		// sem
		if (p + 1 < k) {
			tuple<ll,int,int> nv = { s, p + 1, qt };
			q.push (nv);
			if (s * v[p+1] <= n) {
				q.push ( { s * v[p+1], p + 1, qt + 1} );
				if ((qt + 1)%2 == 1) res -= n/(s * v[p+1]);
				else res += n/(s * v[p+1]);
			}
		}
	} 
	cout << res << endl;
}
