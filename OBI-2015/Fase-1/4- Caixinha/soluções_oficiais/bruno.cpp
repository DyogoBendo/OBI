#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
//const int N = 100;
int N,M;

int main()
{
	ios::sync_with_stdio(0);
	cin >> N >> M;
	ll res = 0;
	for (int i = 1; i <= M; ++i)
		res += max(0, min(M, N-i-1)-max(1, N-i-M)+1);
	cout << res << "\n";
}

