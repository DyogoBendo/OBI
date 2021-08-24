#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
#include <set>

using namespace std;

int main() {
  int n, m;

  cin >> n >> m;
  
  vector<int> A(n), B(m);
  vector< pair<int, int> > val;

  for (int i = 0; i < n; i++) cin >> A[i];
  for (int j = 0; j < m; j++) {
    cin >> B[j];
    val.push_back(make_pair(B[j], j));
  }

  vector<bool> ok(m, false);

  sort(A.begin(), A.end());
  sort(val.begin(), val.end());

  for (int i = 0, j = 0; i < (int)A.size(); i++) {
    while (j < (int)val.size() && val[j].first < A[i]) j++;
    while (j < (int)val.size() && val[j].first == A[i]) {
      ok[val[j].second] = true;
      j++;
    }
  }

  for (int i = 0; i < (int)val.size(); i++) {
    if (i > 0 && val[i].first == val[i-1].first) continue;

    int k = 0;
    for (int j = i; j < (int)val.size(); j++) {
      if (j > 0 && val[j].first == val[j-1].first) continue;

      while (k < (int)val.size() && val[k].first < val[i].first + val[j].first) k++;
      while (k < (int)val.size() && val[k].first == val[i].first + val[j].first) {
	if (val[k].second > max(val[i].second, val[j].second))
	  ok[val[k].second] = true;
	k++;
      }
    }
  }

  bool yes = true;
  for (int i = 0; i < (int)B.size(); i++)
    if (!ok[i]) {
      printf("%d\n", B[i]);
      yes = false;
      break;
    }

  if (yes)
    printf("sim\n");

  return 0;
}
