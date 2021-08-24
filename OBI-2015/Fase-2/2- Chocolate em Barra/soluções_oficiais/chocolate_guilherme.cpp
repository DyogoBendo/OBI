#include <iostream>

using namespace std;

int N;

bool separa( int a, int b ){
  return (a <= N/2 && b > N/2 );
}

int main(){
  int X1, Y1, X2, Y2;

  cin >> N;
  cin >> X1 >> Y1;
  cin >> X2 >> Y2;
  
  if ( separa(X1,X2) ||
       separa(X2,X1) ||
       separa(Y1,Y2) ||
       separa(Y2,Y1) )
    cout << "S" << endl;
  else  cout << "N" << endl;
  
  return 0;
}
