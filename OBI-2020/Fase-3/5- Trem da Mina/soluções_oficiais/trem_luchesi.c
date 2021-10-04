#include <stdio.h>
#include <assert.h>

/* #define DEBUG */

#define MAX_S (112345)
#define MAX_T (2 * MAX_S)
#define MAX_C (100)
#define oo (MAX_C * MAX_T + 1)
#define min(x,y) ((x <= y) ? x : y)
#define MAX_GRAU (100)

typedef enum {False, True} Boolean;

int grau[MAX_S];
int adj[MAX_S][MAX_GRAU];
int peso[MAX_S][MAX_GRAU];
int dist[MAX_S];
int pai[MAX_S];
Boolean visitado[MAX_S];


int fila[MAX_S];
int onde[MAX_S];
int last;

void promove(int v, int d) {
  int i, p;
  if (dist[v] == oo) {
    fila[++last] = v;
    onde[v] = last;
  }
  dist[v] = d;
  i = onde[v]; p = i / 2;
  while ((i > 1) && (dist[fila[p]] > d)) {
    fila[i] = fila[p];
    onde[fila[p]] = i;
    i = p; p = i / 2;
  }
  fila[i] = v;
  onde[v] = i;
}

int pop() {
  int res, v, fe, fd, i, f;
  res = fila[1];
  v = fila[last--];
  i = 1; 
  for (;;) {
    fe = 2 * i;
    fd = fe + 1;
    if (fe > last) break;
    f = fe;
    if ((fd <= last) && (dist[fila[fe]] > dist[fila[fd]])) f = fd;
    if (dist[v] < dist[fila[f]]) break;
    fila[i] = fila[f]; onde[fila[i]] = i;
    i = f;
  }
  fila[i] = v; onde[v] = i;
  return res;
}

int main(int argc, char *noargs[]) {
  int s, t, q, x, m;
  int u, v, w, c, i, res, new_res;

  // lê grafo
  scanf("%d %d", &s, &t);
  for (v = 1; v <= s; ++v) grau[v] = 0;
  for (i = 0; i < t; ++i) {
    scanf("%d %d %d", &v, &w, &c);
    adj[v][grau[v]] = w; adj[w][grau[w]] = v;
    peso[v][grau[v]] = peso[w][grau[w]] = c;
    ++grau[v]; ++grau[w];
    assert ((grau[v] <= MAX_GRAU) && (grau[w] <= MAX_GRAU));
  }

  // processa queries
  scanf("%d", &q);
  while (q-- > 0) {
    scanf("%d %d", &x, &m);

    // determina árvore de distância
    for (v = 1; v <= s; ++v) dist[v] = oo;
    last = 0;
    promove(x, 0);
    pai[x] = x;
    while (last > 0) {
#ifdef dEBUG
      for (i = 1; i <= last; ++i) {
	v = fila[i];
	fprintf (stderr, "%d: onde = %d i = %d\n", v, onde[v], i);
      }
#endif
      v = pop();
      for (i = 0; i < grau[v]; ++i) {
	int new_dist;
	w = adj[v][i];
	new_dist = dist[v] + peso[v][i];
#ifdef DEBUG
	fprintf(stderr, "v %d w %d dist[w] %d new_dist %d\n", v, w, dist[w], new_dist);
#endif
	if (dist[w] > new_dist) {
	  pai[w] = v;
	  promove (w, new_dist);
	}
      }
    }
#ifdef DEBUG
    for (v = 1; v <= s; ++v) fprintf(stderr, "%d: dist = %d pai = %d\n", v, dist[v], pai[v]);
#endif
    // examina cada aresta fora da árvore
    res = oo;
    for (v = 1; v <= s; ++v)
      for (i = 0; i < grau[v]; ++i) {
	w = adj[v][i];
	if ((v > w) || (dist[v] == oo) || (dist[w] == oo) ||
	    (pai[w] == v) || (pai[v] == w)) continue;
#ifdef DEBUG
	fprintf(stderr, "aresta %d %d", v, w);
#endif
	for (u = 1; u <= s; ++u) visitado[u] = False;
	u = v;
	do {
	  visitado[u] = True;
	  u = pai[u];
	} while (u != x);
	visitado[x] = True;
	u = w;
	while (! visitado[u]) u = pai[u];
	new_res = (dist[v] + dist[w] - 2 * dist[u] + peso[v][i] >= m) ?
	  dist[v] + dist[w] + peso[v][i] : oo;
	res = min(res, new_res);
#ifdef DEBUG
	fprintf(stderr, ": %d\n", new_res);
#endif
      }

    // saída
    if (res == oo) res = -1;
    printf("%d\n", res);
  }
  return 0;
}
