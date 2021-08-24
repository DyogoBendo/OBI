#include <cstdio>
#include <vector>
using namespace std;

struct point
{
	int r, c;
	point(int r=0, int c=0) : r(r), c(c) { }
};

int abs(int n)
{
    if (n >= 0)
        return n;
    return -n;
}

int manhattan_distance(int r0, int c0, int r1, int c1)
{
	return abs(r1 - r0) + abs(c1 - c0);
}

int main()
{
	int N, K;
	scanf(" %d %d", &N, &K);

	// posicoes possiveis para o primeiro ponto segundo a primeira dica
	vector<point> possible_positions;
	point p;
	int d;
	scanf(" %d %d %d", &p.r, &p.c, &d);
	for (int r=0; r<N; ++r)
		for (int c=0; c<N; ++c)
			if (manhattan_distance(r, c, p.r, p.c) == d)
				possible_positions.push_back(point(r, c));

	// eliminando posicoes impossiveis segundo as dicas restantes
	for (int k=1; k<K; ++k)
	{
		scanf(" %d %d %d", &p.r, &p.c, &d);
		vector<point> old = possible_positions;
		possible_positions.clear();
		for (int i=0; i<(int)old.size(); ++i)
			if (manhattan_distance(p.r, p.c, old[i].r, old[i].c) == d)
				possible_positions.push_back(old[i]);
	}

	// imprimindo resposta
	if ((int)possible_positions.size() != 1)
		printf("-1 -1\n");
	else
		printf("%d %d\n", possible_positions[0].r, possible_positions[0].c);

	return 0;
}
