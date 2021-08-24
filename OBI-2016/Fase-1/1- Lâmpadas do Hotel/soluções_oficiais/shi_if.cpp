#include <bits/stdc++.h>

using namespace std;


int st[2][2];

int main (void) {
	int ia, ib;
	int fa, fb;
	cin >> ia >> ib >> fa >> fb;

	if (ia == fa and ib == fb) cout << 0 << endl;
	else if (ia == 1 and ib == 1) {
		if ((fa == 0 and fb == 0) or (fa == 0 and fb == 1)) cout << 1 << endl;
		else cout << 2 << endl;
	} else if (ia == 1 and ib == 0) {
		if ((fa == 0 and fb == 0) or (fa == 0 and fb == 1)) cout << 1 << endl;
		else cout << 2 << endl;
	} else if (ia == 0 and ib == 1) {
		if ((fa == 1 and fb == 0) or (fa == 1 and ib == 1)) cout << 1 << endl;
		else cout << 2  << endl;
	} else {
		if ((fa == 1 and fb == 1) or (fa == 1 and fb == 0)) cout << 1 << endl;
		else cout << 2 << endl;
	}

	return 0;	
}
