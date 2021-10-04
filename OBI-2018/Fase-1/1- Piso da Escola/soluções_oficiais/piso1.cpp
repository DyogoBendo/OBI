#include <iostream>
using namespace std;

int main(){
  int L,C,T1,T2;
  
  cin >> L >> C;
  
  T1 = L*C + (L-1)*(C-1);
  T2 = (L-1)*2 + (C-1)*2;
  
  cout << T1 << endl;
  cout << T2 << endl;
    
  return 0;
}
