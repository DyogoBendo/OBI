// Guilherme A. Pinto, OBI-2017, taxa

#include <iostream>
#include <iomanip>
#include <cstring>

using namespace std;

#define MAX 200
#define INF 1000000007
#define menos1(a) ((a+N-1)%N)

int N, s[MAX][MAX], dp[MAX][MAX];

int sum( int i, int j ){
  if ( s[i][j] != -1 ) return s[i][j];
  return s[i][j] = sum( i, menos1( j ) ) + s[j][j];
}

int solve( int i, int j ){
  int res, k, m;
  if ( dp[i][j] != -1 ) return dp[i][j];
  for ( res = INF, k = j; k != i; k = menos1( k ) ){
    m = max( sum( i, menos1( k ) ), sum( k, j ) );
    res = min( res, m + solve( i, menos1( k ) ) + solve( k, j ) );
  }
  return dp[i][j] = res;
}

int main(){
  double F;
  int i, j, menor;
  
  cin >> N >> F;

  memset( dp, -1, sizeof dp );
  memset( s, -1, sizeof s );
  
  for ( i = 0; i < N; i++ )
    dp[i][i] = 0, cin >> s[i][i];
  
  for ( menor = INF, i = 0; i < N; i++ )
    menor = min( menor, solve( i, menos1( i ) ) );

  cout << fixed << setprecision( 2 );
  cout << menor * F << endl;
  
  return 0;
}
