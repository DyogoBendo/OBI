#include <cstdio>

int main(void){
	int N, pt;
	scanf("%d %d",&N,&pt);

	int res = 0;
	for(int i = 0; i < N; i++){
		int a,b;
		scanf("%d %d",&a,&b);
		res += (a+b) >= pt;
	}

	printf("%d\n",res);
	return 0;
}
