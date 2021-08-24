#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue>
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 

using namespace std; 

typedef long long ll; 
typedef pair<int, int> pii;

#define INF 1000000000
#define pb push_back 
#define itr iterator 
#define sz size() 
#define mp make_pair

struct BIT {
	int tree[110000];
	
	void add(int idx, int delta) {
		while (idx <= 100100) {
			tree[idx] += delta;
			idx += idx&-idx;
		}
	}

	int read(int idx) {
		int s = 0;
		while (idx > 0) {
			s += tree[idx];
			idx -= idx&-idx;
		}
		return s;
	}
};

int n, q, op, x, rr;
int treeColuna[110000];
int treeLinha[110000];
pair<int, int> ultLinha[110000], ultColuna[110000];

BIT ColunaFreq[51], LinhaFreq[51];
int temp[51];

int main() {
	scanf("%d %d", &n, &q);
	for (int i = 1; i <= q; i++) {
		int best = -1;
		int best_val = -1;
		int temp = 0;
		int tot = 0;

		scanf("%d %d", &op, &x);
		if (op == 1) {
			scanf("%d", &rr);
			if (ultLinha[x].first != 0)
				ColunaFreq[ultLinha[x].second].add(ultLinha[x].first, -1);
			ultLinha[x] = make_pair(i, rr);
			ColunaFreq[rr].add(i, 1);
		}
		else if (op == 2) {
			scanf("%d", &rr);
			if (ultColuna[x].first != 0)
				LinhaFreq[ultColuna[x].second].add(ultColuna[x].first, -1);
			ultColuna[x] = make_pair(i, rr);
			LinhaFreq[rr].add(i, 1);
		}
		else if (op == 3) {
			for (int val = 0; val <= 50; val++) if (val != ultLinha[x].second) {
				int cnt = LinhaFreq[val].read(i) - LinhaFreq[val].read(ultLinha[x].first);
				tot += cnt;

				if (cnt >= best) {
					best = cnt;
					best_val = val;
				}
			}

			if (n-tot > best || (n-tot == best && best_val < ultLinha[x].second)) {
				best_val = ultLinha[x].second;
			}

			printf("%d\n", best_val);
		}
		else if (op == 4) {
			for (int val = 0; val <= 50; val++) if (val != ultColuna[x].second) {
				int cnt = ColunaFreq[val].read(i) - ColunaFreq[val].read(ultColuna[x].first);
				tot += cnt;

				if (cnt >= best) {
					best = cnt;
					best_val = val;
				}
			}

			if (n-tot > best || (n-tot == best && best_val < ultColuna[x].second)) {
				best_val = ultColuna[x].second;
			}

			printf("%d\n", best_val);
		}
	}
}
