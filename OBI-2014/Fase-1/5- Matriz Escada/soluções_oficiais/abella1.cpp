#include <iostream>
#include <cstdio>

using namespace std;

int main() {
  int n, m;

  scanf("%d %d", &n, &m);

  int zero_up_to = -1;
  bool ok = true;

  for (int y = 0; y < n; y++) {
    int first_nonzero = m;

    for (int x = 0; x < m; x++) {
      int v;
      scanf("%d", &v);

      if (v != 0) {
	if (x <= zero_up_to)
	  ok = false;
	if (first_nonzero == m)
	  first_nonzero = x;
      }
    }

    zero_up_to = first_nonzero;
  }

  printf(ok ? "S\n" : "N\n");

  return 0;
}
