#include <cstdio>
#include <map>

using namespace std;

int main () {
  int n;
  
  scanf ("%d", &n);
  
  map<int, int> e, d;
  int cnt = 0;
  while (n--) {
    int t;
    char l;
    scanf ("%d %c", &t, &l);
    if (l == 'D') {
      if (e[t]>0) ++cnt, e[t]--;
      else d[t]++;
    } else {
      if (d[t]>0) ++cnt, d[t]--;
      else e[t]++;
    }
  }
  printf ("%d\n", cnt);
  
  return 0;
}
