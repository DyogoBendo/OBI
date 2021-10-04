// piso de atlanta
// obi2020 - fase 3

#include <iostream>

using namespace std;

int main(void) {
  int a, b, larg, compr;
  
  cin >> a >> b;

  for(int x = 1; x <= b; x++) {
    if (b % x != 0)
      continue;
    larg = b/x + 2;
    compr = x + 2;
    if (a == 2*(compr+larg) - 4) {
      cout << compr << " " << larg << endl;
      return 0;
    }
  }
  cout << -1 << " " << -1 << endl;
  return 0;
}
