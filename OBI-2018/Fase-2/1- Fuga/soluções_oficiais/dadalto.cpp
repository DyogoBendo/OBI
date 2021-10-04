#include <stdio.h>
#include <string.h>

/*
 O problema na verdade pode ser resolvido em tempo O(N*M) ou até em tempo constante,
 mas a princípio coloquei como solução o backtracking (também pode ser melhorado com alguma poda no backtracking). 
 Se precisar dificultar, dá pra colocar valores maiores de N e M.
 A solução é um caminho máximo no grafo das células de coordenadas ímpares (vértices são os asteriscos). 
	
	*-*-*-*
	|#|#|#|
	*-*-*-*
	|#|#|#|
	*-*-*-*
	|#|#|#|
	*-*-*-*

 Sempre é possível derrubar os armários para forçar o caminho máximo como único caminho 
 e obviamente não dá pra fazer melhor que o caminho máximo. 
 Também não é possível bloquear completamente o caminho entre a entrada e a saída 
 já que os dois ficam na borda do grid (é fácil ver tentando fazer um corte no grafo).
*/

char grid[1123][1123];
int n , m;
int xf, yf;

void print_grid()
{
	for (int i = 1; i <= n ; i++, fprintf(stderr, "\n"))
		for (int j = 1; j <= m ; j++)
			fprintf(stderr, "%c", grid[i][j]);
	fprintf(stderr, "\n");
}

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int best = 0;

void foo(int x, int y, int k)
{
	if (x == xf && y == yf && k > best)
	{
		best = k;
		fprintf(stderr, "%d\n", k);
		print_grid();
	}
	else
	{
		char tmp[4];
		for (int i = 0; i < 4; i++)
			tmp[i] = grid[x + dx[i]][y + dy[i]];
		for (int i = 0; i < 4; i++)
		{
			if (grid[x + dx[i]][y + dy[i]] == '.')
			{
				for (int j = 0; j < 4; j++)
					if (grid[x + dx[j]][y + dy[j]] == '.')
						grid[x + dx[j]][y + dy[j]] = '#';

				grid[x + dx[i]][y + dy[i]] = '@';

				foo(x + dx[i], y + dy[i], k + 1);

				for (int j = 0; j < 4; j++)
					grid[x + dx[j]][y + dy[j]] = tmp[j];
			}
		}
	}
}

int main(void)
{
	int xi, yi;
	scanf("%d %d %d %d %d %d", &n, &m, &xi, &yi, &xf, &yf);
	memset(grid, '#', sizeof(grid));
	for (int i = 1 ; i <= n; i++)
		for (int j = 1; j <= m; j++)
			if (i % 2 || j % 2)
				grid[i][j] = '.';
	print_grid();

	grid[xi][yi] = '@';
	foo(xi, yi, 1);
	printf("%d\n", best);
}