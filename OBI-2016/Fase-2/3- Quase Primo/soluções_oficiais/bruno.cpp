#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int n, k, res;
vector<int> vet;

void solve(int a, int p, ll k)
{
	if (k > n) return;
	if (p == -1)
	{
		if (k == 1) return;
		res += (a%2 == 1 ? -1 : 1) * n / k;
		return;
	}
	solve(a, p-1, k);
	solve(a+1, p-1, k*vet[p]);
}

int main()
{
	cin >> n >> k;
	for (int i = 0; i < k; ++i)
	{
		int x; cin >> x; vet.push_back(x);
	}
	res = n;
	solve(0, k-1, 1);
	cout << res << endl;
}

