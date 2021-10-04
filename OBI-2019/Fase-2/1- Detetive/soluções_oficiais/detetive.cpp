//#include <bits/stdc++.h> nao funciona no meu mac...

#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

vector<vector<int> > implica;
vector<vector<int> > implicado_por;
vector<set<int> > causa;

vector<int> prova;
vector<char> ocorreu;

void consequencias(int x) {
	queue<int> Q;
	Q.push(x);
	ocorreu[x] = 1;

	while (!Q.empty()) {
		x = Q.front();
		Q.pop();

		for (int i = 0; i < implica[x].size(); i++)
			if (!ocorreu[implica[x][i]]) {
				ocorreu[implica[x][i]] = 1;
				Q.push(implica[x][i]);
			}
	}
}

void busca_causa(int x) {
	if (implicado_por[x].size() == 0)
		causa[x].insert(x);
	else {
		
		for (int i = 0; i < implicado_por[x].size(); i++) {
			if (causa[implicado_por[x][i]].size() == 0)
				busca_causa(implicado_por[x][i]);

			for (set<int>::iterator it = causa[implicado_por[x][i]].begin(); it != causa[implicado_por[x][i]].end(); it++)
				causa[x].insert(*it);
		}
	}
}

int main(void) {
	int d, m, n;
	scanf("%d%d%d", &d, &m, &n);	

	ocorreu.resize(d, 0);
	implica.resize(d);
	implicado_por.resize(d);
	causa.resize(d);

	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		a--; b--;
		implica[a].push_back(b);
		implicado_por[b].push_back(a);
	}

	for (int i = 0; i < n; i++) {
		int a;
		scanf("%d", &a);
		a--;
		prova.push_back(a);
		ocorreu[a] = 1;
		consequencias(a);
	}

	for (int i = 0; i < d; i++)
		if (causa[i].size() == 0)
			busca_causa(i);

	for (int i = 0; i < d; i++)
		if (!ocorreu[i]) {
			char possible = 1;
			for (int j = 0; j < prova.size() && possible; j++) {
				char skip = 1;
				for (set<int>::iterator it = causa[prova[j]].begin(); it != causa[prova[j]].end() && skip; it++)
					if (causa[i].find(*it) == causa[i].end())
						skip = 0;

				if (!skip) continue;
				ocorreu[i] = 1;
				consequencias(i);
				possible = 0;
			}				
		}
	
	// imprime o resultado
	char space = 0;
	for (int i = 0; i < d; i++) {
		if (ocorreu[i]) {
			if (space) printf(" ");
			space = 1;
			printf("%d", i + 1);
		}
	}
	printf("\n");

	return 0;
}
