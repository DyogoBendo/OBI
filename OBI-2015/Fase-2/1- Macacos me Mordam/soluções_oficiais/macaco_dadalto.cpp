/****************************************************************************
 * Arthur Pratti Dadalto
 * OBI 2015 - Macaco
 * Convex hull com line sweep
 ***************************************************************************/

#include <stdio.h>
#include <algorithm>

struct point{
	long long x, y;
	bool operator < (point a) const { return x < a.x || (x == a.x && y < a.y); }
} p[1123456];

int ch[1123456], nch;

long long cross(point p0, point p1, point p2)
{
	return (p1.x - p0.x)*(p2.y - p0.y) - (p2.x - p0.x)*(p1.y - p0.y);
}

int
main(void)
{
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		scanf("%lld %lld", &p[i].x, &p[i].y);
	std::sort(p, p+n);
	for(int i = 0; i < n; ch[nch++] = i, i++)
		while(nch >= 2 && cross(p[ch[nch-2]], p[ch[nch-1]], p[i]) >= 0)
			nch--;
	printf("%d\n", nch - 1);
}