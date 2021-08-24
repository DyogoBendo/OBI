#include <stdio.h>
#include <stdbool.h>

typedef struct
{
  int x, y;
}
point_t;

typedef struct
{
  point_t p;
  int d;
}
hint_t;

#define HMAX 100
static hint_t H [HMAX];

static int
dist (point_t p, point_t q)
{
  int dx = q.x-p.x;
  if (dx < 0)
    dx = -dx;
  int dy = q.y-p.y;
  if (dy < 0)
    dy = -dy;
  return dx + dy;
}

static bool
test (int n, int k, int x, int y)
{
  int i;
  if (x < 0 || x >= n || y < 0 || y >= n)
    return false;
  point_t p = {x, y};
  for (i = 1; i < k; ++i)
    if (dist(p, H[i].p) != H[i].d)
      return false;
  return true;
}

int
main ()
{
  int i, n, k;
  scanf ("%d%d", &n, &k);
  for (i = 0; i < k; ++i)
    scanf ("%d%d%d", &H[i].p.x, &H[i].p.y, &H[i].d);
  int x = H[0].p.x;
  int y = H[0].p.y;
  int d = H[0].d;
  point_t treasure;
  if (d == 0)
    treasure = (point_t) {x, y};
  else
    {
      bool found = false;
      for (i = 0; i < d; ++i)
        {
          if (test (n, k, x-d+i, y+i))
            {
              if (found)
                goto many;
              treasure = (point_t) {x-d+i, y+i};
              found = true;
            }
          if (test (n, k, x+i, y+d-i))
            {
              if (found)
                goto many;
              treasure = (point_t) {x+i, y+d-i};
              found = true;
            }
          if (test (n, k, x+d-i, y-i))
            {
              if (found)
                goto many;
              treasure = (point_t) {x+d-i, y-i};
              found = true;
            }
          if (test (n, k, x-i, y-d+i))
            {
              if (found)
                goto many;
              treasure = (point_t) {x-i, y-d+i};
              found = true;
            }
        }
    }
  printf ("%d %d\n", treasure.x, treasure.y);
  return 0;
many:
  puts ("-1 -1");
  return 0;
}


