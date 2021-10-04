/*
	Matheus Leal V

	OBI 2019 - Fase 03 - Exploração

	Complexidade O(N*log(N))
*/
#include <bits/stdc++.h>
#define N 500010
#define f first
#define s second
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pii;

int n;

ll P, Q, val[N], bit[N], ans;

pii v[N];

vector<ll> comp;

void upd(int x, ll v)
{
	for(int i = x; i < N; i += (i&-i)) bit[i] += v;
}

ll query(int x)
{
	ll sum = 0;

	for(int i = x; i > 0; i -= (i&-i)) sum += bit[i];

	return sum;
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	cin>>n>>P>>Q;

	if(Q < 0)
	{
		P *= -1LL;

		Q *= -1LL;
	}

	for(int i = 1; i <= n; i++)
	{
		cin>>v[i].f>>v[i].s;

		ll k = Q*v[i].s - P*v[i].f;

		comp.push_back(k);
	}

	sort(comp.begin(), comp.end());

	comp.erase(unique(comp.begin(), comp.end()), comp.end());

	sort(v + 1, v + n + 1);

	for(int i = 1; i <= n; i++)
	{
		ll k = Q*v[i].s - P*v[i].f;

		k = upper_bound(comp.begin(), comp.end(), k) - comp.begin();
		ans += query(k);

		upd(k, 1);
	}

	cout<<ans<<"\n";
}