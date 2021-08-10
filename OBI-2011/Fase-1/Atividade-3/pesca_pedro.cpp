#include <cstdio>
#include <cassert>

const int MAX_N = 100;
int N;
int x1[MAX_N], x2[MAX_N], y1[MAX_N], y2[MAX_N];	

int main(){
	
	scanf("%d", &N);
	assert(N >= 1 && N <= 100);

	for(int i = 0; i < N; i++){
		scanf("%d%d%d%d", &x1[i], &x2[i], &y1[i], &y2[i]);
		assert(x1[i] <= x2[i]);
		assert(y1[i] <= y2[i]);
		assert(x1[i] >= 1 && x1[i] <= 100 && x2[i] >=1 && x2[i] <= 100);
		assert(y1[i] >= 1 && y1[i] <= 100 && y2[i] >= 1 && y2[i] <= 100);
	}
	int area = 0;
	for(int i = 1; i < 100; i++){
		for(int j = 1; j < 100; j++){
			bool in = false;
			for(int k = 0; k < N; k++){
				if(x1[k] <= i && i < x2[k] && y1[k] <= j && j < y2[k]){
					in = true;
				}
			}
			if(in){
				area++;
			}
		}
	}	
	printf("%d\n", area);

	return 0;
}
