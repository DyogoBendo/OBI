#include <stdio.h>
#include <algorithm>
using namespace std;
const int MAXN=100010;
const int INF=1000000000;
int n,k;
int num[MAXN];
int main()
{
	scanf("%d %d",&n,&k);
	for(int i=1;i<=n;i++)
	{
		scanf("%d",&num[i]);
	}
	//ordenando os numeros
	sort(&num[1],&num[n+1]);
	int minimo=INF;
	for(int i=0;i<=k;i++)
	{
		//encontrando o minimo se vender os i
		//menores predios
		minimo=min(minimo,num[n-(k-i)]-num[i+1]);
	}
	printf("%d\n",minimo);
	return 0;
}