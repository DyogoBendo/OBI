/*******************/
/* taxa            */
/* r. anido        */
/* OBI2017         */
/*******************/

#include <stdio.h>
#include <limits.h>

#define MAXSIZE 200
#define MAXVAL INT_MAX
#define max(x,y) (x > y ? x : y)

int n,  // number of properties
  val[MAXSIZE],
  sum[2*MAXSIZE],
  cost[2*MAXSIZE-1][2*MAXSIZE-1];
double v;

int main (int argc, const char * argv[])
{
  int  i, j, k, l, q, q1;

  scanf("%d %lf", &n, &v);
  for (i=0; i<n; i++)
    scanf("%d", &val[i]);
  // pre-computa somas
  sum[0] = 0;
  for (i=1; i<2*n; i++)
    sum[i] = sum[i-1] + val[(i-1)%n];
  // inicializa tabela de custos
  for (i=0; i<2*n - 1; i++)
    cost[i][i] = 0;
  for (i=0; i<2*n-2; i++) {
    j = i + 1;
    cost[i][j] = max(val[i % n], val[j % n]);
  }
  // computa todos os custos
  for (l=3; l<n+1; l++) {
    for (i=0; i>=0 && i<2*n-l; i++) {
      j = i + l - 1;
      q = MAXVAL;
      for (k=i; k<j; k++) {
	q1 = cost[i][k] + cost[k+1][j] + max(sum[k+1]-sum[i], sum[j+1]-sum[k+1]);
	if (q1 < q)
	  q = q1;
      }
      cost[i][j] = q;
    }
  }
  // agora acha o minimo
  q = cost[0][n-1];
  for (i=1; i<n; i++) {
    j = i + n -1;
    if (cost[i][j] < q)
      q = cost[i][j];
  // imprime o resultado
  }
  printf("%.2lf\n", v*q);

  return 0;
}
