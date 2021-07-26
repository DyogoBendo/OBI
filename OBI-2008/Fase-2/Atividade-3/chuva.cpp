#include <stdio.h>

#include <algorithm>
#include <utility>
#include <set>

using namespace std;

#define wipe(v, x) memset((v), (x), sizeof(v))

const int INF = 0x3f3f3f3f;

int N, xi, yi, xf, yf;
int x1[3010], y1[3010], x2[3010], y2[3010];
int cost[3010][3010];
int dist[3010], marc[3010];

struct index_lt {
	bool operator ()(const int a, const int b) const {
		if (int t = dist[a] - dist[b]) return t < 0;
		return a < b;
	}
};

set<int, index_lt> heap;

int main() {
	scanf(" %d %d %d %d", &xi, &yi, &xf, &yf);
	scanf(" %d", &N);
	for (int i = 0; i < N; i++) {
		scanf(" %d %d %d %d", &x1[i], &y1[i], &x2[i], &y2[i]);
	}
	x1[N] = xi; y1[N] = yi;
	x1[N+1] = xf; y1[N+1] = yf;

	x2[N] = x1[N];
	y2[N] = y1[N];
	x2[N+1] = x1[N+1];
	y2[N+1] = y1[N+1];
	N += 2;
	wipe(cost, INF);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int dx = max(0, max(x1[i], x1[j]) - min(x2[i], x2[j]));
			int dy = max(0, max(y1[i], y1[j]) - min(y2[i], y2[j]));
			cost[i][j] = dx + dy;
		}
	}
	wipe(dist, INF);
	wipe(marc, 0);
	dist[N-2] = 0;
	heap.insert(N-2);
	while (!heap.empty()) {
		int top = *heap.begin(); heap.erase(top);
		marc[top] = 1;
		for (int i = 0; i < N; i++) {
			if (marc[i]) continue;
			int ndist = dist[top] + cost[top][i];
			if (ndist < dist[i]) {
				heap.erase(i);
				dist[i] = ndist;
				heap.insert(i);
			}
		}
	}
	printf("%d\n", dist[N-1]);
	return 0;
}
