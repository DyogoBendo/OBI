#include <stdio.h>

int main() {
   int N;
   scanf(" %d", &N);
   int time = N - 1986;
   int ans = 2062 + time - (time % 76);
   printf("%d\n", ans);
   return 0;
}
