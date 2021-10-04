// piso de atlanta
// obi2020 - fase 3

#include <iostream>

using namespace std;

const int MAX = 1003;

int main(void) {
  int borda, centro, x, y;
  cin >> borda >> centro;
  
  for (x = 3; x < MAX; x++) {
    for (y = x; y >= 3; y--) {
      if (borda+centro == x*y && borda == 2*x+2*y-4) {
	cout << y << " " << x << endl;
	return 0;
      }
    }
  }
  cout << "-1 -1" << endl;

  return 0;
}
