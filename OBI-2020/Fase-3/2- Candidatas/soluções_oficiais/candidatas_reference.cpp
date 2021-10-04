// sequencias
// obi2020 - fase 3

#include <iostream>
#include <vector>
using namespace std;

#define x first
#define y second

typedef pair<int, int> pii;
typedef long long ll;

const int MAXN = 100100;

int n, m, sequencia[MAXN];

int mdc(int a, int b) {
  while (b) {
    a %= b;
    swap(a, b);
  }
  return a;
}

struct No {
  vector<pii> l, r;
  ll cnt;
  // first: comprimento
  // second: mdc
  
  No() : cnt(0) {
  }
  
  No(int val) {
    l = r = {{0, 0}, {1, val}};
    cnt = (val != 1) ? 1 : 0;
  }
  static void expande(vector<pii> &ret, const vector<pii> &add) {
    int sz_init = ret.back().x;
    for (auto it : add) {
      int sz = sz_init + it.x;
      if (it.y % ret.back().y == 0) ret.back().x = sz;
      else ret.push_back({sz, mdc(it.y, ret.back().y)});
    }
  }
  
  friend No operator+(const No &a, const No &b) {
    if (a.l.empty()) return b;
    if (b.l.empty()) return a;
    
    No ret;
    ret.l = a.l;
    ret.r = b.r;
    expande(ret.l, b.l);
    expande(ret.r, a.r);
    ret.cnt = a.cnt + b.cnt;
    int rt = (int)b.l.size() - 1;
    for (int lt = 1; lt < (int)a.r.size(); ++lt) {
      while (rt > 0 && mdc(a.r[lt].y, b.l[rt].y) == 1)
	--rt;
      ret.cnt += (ll)(a.r[lt].x - a.r[lt - 1].x) * b.l[rt].x;
    }
    return ret;
  }
};

struct Seg {
  static const int off = 1 << 17;
  No data[2 * off];
  int from, to;

  void atualiza(int pos, int val) {
    pos += off;
    data[pos] = No(val);
    for (pos /= 2; pos > 0; pos /= 2)
      data[pos] = data[2 * pos] + data[2 * pos + 1];
  }

  No consulta(int nd, int lo, int hi) {
    if (lo >= to || hi <= from) return No();
    if (lo >= from && hi <= to) return data[nd];
    int mid = (lo + hi) / 2;
    return consulta(2 * nd, lo, mid) + consulta(2 * nd + 1, mid, hi);
  }

  ll consulta(int l, int r) {
    from = l, to = r;
    return consulta(1, 0, off).cnt;
  }

  void constroi() {
    for (int i = 0; i < n; ++i)
      data[i + off] = No(sequencia[i]);
    for (int i = off - 1; i > 0; --i)
      data[i] = data[2 * i] + data[2 * i + 1];
  }
} S;

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; ++i)
    cin >> sequencia[i];

  S.constroi();

  for (int i = 0; i < m; ++i) {
    int t, a, b;
    cin >> t >> a >> b;
    if (t == 1)
      S.atualiza(a - 1, b);
    else
      cout << S.consulta(a-1, b) << endl;
  }
  return 0;
}
