// OBI2020
// camisetas

#include <cstdio>
using namespace std;

int x, n;
int pref[3];
int prod_p;
int prod_m;

int main () {
  
  scanf("%d", &n);
  for (int i=0; i<n; i++) {
    scanf("%d", &x);
    pref[x]++;
  }
  scanf("%d", &prod_p);
  scanf("%d", &prod_m);

  if (prod_p >= pref[1] && prod_m >= pref[2])
    printf("S\n");
  else
    printf("N\n");
}
