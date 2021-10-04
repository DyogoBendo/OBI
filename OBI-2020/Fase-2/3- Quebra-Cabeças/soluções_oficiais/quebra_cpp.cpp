#include <cstdio>
#include <climits>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAX = 505;
const int MIN = -1e9;

int n;
int elem_linha0, elem_linha1;
int linha0[MAX], linha1[MAX];
int tab[2][MAX][MAX];

int pd() {
  int uma = 1;
  int outra = 1 - uma;
  for (int i=0; i<=elem_linha0; i++)
    for (int j=0; j<=elem_linha1; j++)
      tab[uma][i][j] = MIN;

  tab[uma][elem_linha0][elem_linha1] = 0;
  tab[outra][elem_linha0][elem_linha1] = 0;

  for (int k=0; k<n; k++) {
    for (int i=elem_linha0; i>=0; i--) {
      for (int j=elem_linha1; j>=0; j--) {
	if (i == elem_linha0 && j == elem_linha1)
	  continue;
	tab[outra][i][j] = MIN;
	if (i < elem_linha0)
	  tab[outra][i][j] = max(tab[outra][i][j], tab[uma][i+1][j]);
	if (j < elem_linha1)
	  tab[outra][i][j] = max(tab[outra][i][j], tab[uma][i][j+1]);
	if (i < elem_linha0 && j < elem_linha1)
	  tab[outra][i][j] = max(tab[outra][i][j],linha0[i]*linha1[j] + tab[uma][i+1][j+1]);
      }
    }
    uma = 1 - uma;
    outra = 1 - uma;
  }
  return tab[uma][0][0];
}

int main()
{
  scanf("%d", &n);

  scanf("%d", &elem_linha0); 
  for (int i=0; i<elem_linha0; i++)
    scanf("%d", &linha0[i]);
  scanf("%d", &elem_linha1);
  for (int i=0; i<elem_linha1; i++)
    scanf("%d", &linha1[i]);

  printf("%d\n", pd());
}
