#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

void bit_add(vector<int> &bit, int x, int val) {
  for (int x2 = max(x+1, 1); x2 <= (int)bit.size(); x2 += x2&-x2)
    bit[x2-1] += val;
}

int bit_get(vector<int> &bit, int x) {
  int ret = 0;
  for (int x2 = min(x+1, (int)bit.size()); x2 >= 1; x2 -= x2&-x2)
    ret += bit[x2-1];
  return ret;
}

struct halfsolver {
  int n, nq, nc;
  vector <vector <int> > colorbit;

  vector <int> colsetwhen, colsetcolor;
  vector <int> linesetwhen, linesetcolor;

  halfsolver(int n, int nq, int nc): n(n), nq(nq), nc(nc) {
    colorbit = vector <vector<int> >(nc, vector<int>(nq, 0));

    colsetwhen = vector<int>(n, -1);
    colsetcolor = vector<int>(n, 0);

    linesetwhen = vector<int>(n, -1);
    linesetcolor = vector<int>(n, 0);
  }

  void set_line(int q, int x, int color) {
    linesetwhen[x] = q;
    linesetcolor[x] = color;
  }

  void set_col(int q, int x, int color) {
    if (colsetwhen[x] != -1) {
      int old_color = colsetcolor[x];
      int old_time = colsetwhen[x];

      bit_add(colorbit[old_color], old_time, -1); 
    }

    colsetwhen[x] = q;
    colsetcolor[x] = color;
    bit_add(colorbit[color], q, +1);
  }

  int line_most_freq(int q, int x) {
    vector<int> many(nc, 0);

    for (int i = 0; i < nc; i++)
      if (i != linesetcolor[x])
	many[i] = bit_get(colorbit[i], q) - bit_get(colorbit[i], linesetwhen[x]);

    many[linesetcolor[x]] = n - accumulate(many.begin(), many.end(), 0);

    return nc-1-(max_element(many.rbegin(), many.rend()) - many.rbegin());
  }
};

int main() {
  int n, q;

  cin >> n >> q;
  
  const int nc = 50+1;
  struct halfsolver h1(n, q, nc), h2(n, q, nc);

  for (int i = 0; i < q; i++) {
    int op, x, color;
    
    cin >> op >> x; x--;
    if (op <= 2) cin >> color;

    if (op == 1) {
      h1.set_line(i, x, color);
      h2.set_col(i, x, color);
    } else if (op == 2) {
      h1.set_col(i, x, color);
      h2.set_line(i, x, color);
    } else {
      int ret;
      if (op == 3) ret = h1.line_most_freq(i, x);
      else ret = h2.line_most_freq(i, x);
      cout << ret << endl;
    }
  }

  return 0;
}
