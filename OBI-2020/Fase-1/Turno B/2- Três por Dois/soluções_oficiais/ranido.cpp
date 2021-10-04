#include <cstdio>
#include <algorithm>
using namespace std;

#define MAXN 100000

int preco[MAXN];
long long sol = 0;

bool cmp(int a, int b) {
  return a > b;
}

int main(void) {
  int n;

  scanf("%d", &n);
  for (int i=0; i<n; i++)
    scanf("%d", &preco[i]);

  sort(preco, preco+n, cmp);

  for (int i=0; i<n; i++) {
    if (i % 3 == 2) {
      continue;
    }
    sol += preco[i];
  }
  printf("%lld\n", sol);

  return 0;
}
