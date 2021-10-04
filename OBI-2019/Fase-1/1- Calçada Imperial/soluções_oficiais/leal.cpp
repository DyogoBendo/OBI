/*
	Matheus Leal V
	OBI 2019 - Fase 01 - Calçada Imperial
*/

#include <bits/stdc++.h>
#define N 530
using namespace std;

int n, v[N], ans = 1;

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	cin>>n;

	for(int i = 1; i <= n; i++) cin>>v[i];

	for(int i = 1; i <= n; i++)
	{
		for(int j = 1; j <= n; j++)
		{
			if(v[i] == v[j]) continue;

			vector<int> arr(2);

			arr[0] = v[i], arr[1] = v[j];

			int sz = 0, atual = 0;

			for(int t = 1; t <= n; t++)
			{
				if(v[t] == arr[sz])
				{
					sz ^= 1;

					atual ++;
				}
			}

			ans = max(ans, atual);
		}
	}

	cout<<ans<<"\n";

}