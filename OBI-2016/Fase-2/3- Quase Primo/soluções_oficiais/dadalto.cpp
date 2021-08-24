#include <stdio.h>

int p[112];
long long ans = 0;
long long n, k;

void solve(int i, int bits, long long num)
{
	if(num > n)
		return;

	if(i == k)
	{
		if(bits == 0)
			return;
		if(bits & 1)
			ans += n / num;
		else
			ans -= n / num;
	}
	else
		solve(i+1, bits, num), solve(i+1, bits + 1, num * p[i]);
}

int main(void)
{
	scanf("%lld %lld", &n, &k);
	for(int i = 0; i < k; i++)
		scanf("%d", &p[i]);
	solve(0, 0, 1);
	printf("%lld\n", n - ans);
}
