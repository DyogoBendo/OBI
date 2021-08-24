#include <iostream>
using namespace std;

int main () {
  int a, b, c, d;
  cin >> a >> b >> c >> d;
  if (d > (a-c)*b) cout << "PROXIMO VOO" << endl;
  else cout << c + (d-1)/b << " " << char(((d-1)%b) + 'A');
  return 0;
}
