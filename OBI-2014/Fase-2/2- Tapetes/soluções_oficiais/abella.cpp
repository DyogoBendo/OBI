#include <iostream>
#include <cstdio>
 
typedef long long lint;

using namespace std;

int main() {
  int l, n;
  
  cin >> l >> n;

  if (n > l) {
    cout << -1 << endl;
  } else {
    int lastsize = l - (n-1);
    cout << (n-1) + (lint)lastsize * lastsize << endl;
  }

  return 0;
}

