#include <stdio.h>

#define N_NOTAS (6)
#define MAX_S (5000)

int notas[N_NOTAS] = {2, 5, 10, 20, 50, 100};
int n[N_NOTAS];
int memory [MAX_S+1][N_NOTAS];

int resolve(int s, int min_v) {
  int i, q, new_s, res;
  if (min_v == N_NOTAS) {
    if (s == 0) return 1;
    else return 0;
  }
  if (memory[s][min_v] >= 0) return memory[s][min_v];
  res = 0;
  q = s / notas[min_v];
  if (q > n[min_v]) q = n[min_v];
  for (i = 0; i <= q; ++i) {
    new_s = s - i * notas[min_v];
    res += resolve (new_s, min_v + 1);
  }
  /* if (res != 0) */
  /*   fprintf(stderr, "s = %d min_v = %d res = %d\n", s, min_v, res); */
  memory[s][min_v] = res;
  return res;
}

int main(int argc, char *noargs[]) {
  int s;
  int i, v;

  scanf("%d", &s);
  for (v = 0; v < N_NOTAS; ++v) scanf("%d", &n[v]);
  for (i = 0; i <= s; ++i)
    for (v = 0; v < N_NOTAS; ++v)
      memory[i][v] = -1;
  
  printf ("%d\n", resolve(s, 0));
    
  return 0;
}
