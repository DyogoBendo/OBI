#include <stdio.h>

int N;
int R, C;

const int dir[8][2] = {
	{-2, +1},
	{-1, +2},
	{+1, +2},
	{+2, +1},
	{+2, -1},
	{+1, -2},
	{-1, -2},
	{-2, -1},
};

int hole() {
	return (R == 2 && C == 2) ||
	       (R == 3 && C == 5) ||
	       (R == 4 && C == 1) ||
	       (R == 4 && C == 2);
}

int main() {
	scanf("%d", &N);
	R = 4; C = 4;
	for (int i = 0; i < N; i++) {
		int M;
		scanf("%d", &M);
		M--;
		R += dir[M][0];
		C += dir[M][1];
		if (hole()) {
			printf("%d\n", i+1);
			return 0;
		}
	}
	printf("%d\n", N);
	return 0;
}
