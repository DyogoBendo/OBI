#include <cstdio>

int main()
{
	int N, S;
	scanf(" %d %d", &N, &S);
	int delta = S - N * (1 + N*N) / 2;
	int current = 1;
	for (int i=0; i<N; ++i)
	{
		for (int j=0; j<N; ++j)
			if (i == 0 && delta < 0)
				printf("%d ", current++ + delta);
			else if (i == N-1 && delta > 0)
				printf("%d ", current++ + delta);
			else
				printf("%d ", current++);
		printf("\n");
	}
	return 0;
}
