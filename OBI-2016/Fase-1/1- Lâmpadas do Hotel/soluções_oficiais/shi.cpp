#include <bits/stdc++.h>

using namespace std;


int st[2][2];

int main (void) {
	int ia, ib;
	int fa, fb;
	cin >> ia >> ib >> fa >> fb;

	queue < pair<int,int> > q;
	memset (st, -1, sizeof st);
	
	q.push ( make_pair (ia, ib) );
	st[ia][ib] = 0;
	
	while (!q.empty()) {
		int ca = q.front().first;
		int cb = q.front().second;
		q.pop();
		if (st[!ca][cb] == -1) {
			st[!ca][cb] = st[ca][cb] + 1;
			q.push ( make_pair (!ca, cb) );
		}	
		if (st[ca][!cb] == -1) {
			st[!ca][!cb] = st[ca][cb] + 1;
			q.push ( make_pair (!ca, !cb) );
		}
	}
	cout << st[fa][fb] << endl;

	return 0;	
}
