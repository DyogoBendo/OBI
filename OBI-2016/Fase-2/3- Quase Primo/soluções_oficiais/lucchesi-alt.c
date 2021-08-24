#include <stdio.h>

#define MAX_K (40)

long long int p[MAX_K];

long long int resolve(long long int n, int K) {
  long long int res;
  if (K-- == 0) return n;
  res = resolve (n, K);
  if (n >= p[K]) res -= resolve (n / p[K], K);
  return res;
}

int main() {
  long long int N;
  int K, i;
  scanf ("%lld %d", &N, &K);
  for (i = 0; i < K; ++i) scanf("%lld", &p[i]);
  printf("%lld\n", resolve(N, K));
  return 0;
}
