#include <cstdio>

long long n;
int a, b, c;

int parent[110000];
long long size[110000];

int find(int x) {
	if (parent[x] == x) return x;
	return parent[x] = find(parent[x]);
}

void link(int a, int b) {
	int pa = find(a), pb = find(b);
	parent[pb] = pa;
	size[pa] += size[pb]+1;
}

int main() {
	scanf("%lld", &n);

	long long ans = n*(n-1)/2;
	for (int i = 1; i <= n; i++) parent[i] = i;

	for (int i = 0; i < n-1; i++) {
		scanf("%d %d %d", &a, &b, &c);
		if (c == 0) link(a,b);
	}

	for (int i = 1; i <= n; i++) if (parent[i] == i)
		ans -= size[i] * (size[i]+1) / 2;

	printf("%lld\n", ans);
}