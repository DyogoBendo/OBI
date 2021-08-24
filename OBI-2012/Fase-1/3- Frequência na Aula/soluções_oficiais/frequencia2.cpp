#include <cstdio>
#include <cstring>

int freq[1001000];
int N;

int main(){
	scanf("%d", &N);
	memset(freq,0,sizeof freq);
	for(int i = 0; i < N; i++){
		int val;
		scanf("%d", &val);
		freq[val] = 1;
	}
	int ret = 0;
	for(int i = 0; i < 1001000; i++){
		ret += freq[i];
	}
	printf("%d\n", ret);
	return 0;
}
