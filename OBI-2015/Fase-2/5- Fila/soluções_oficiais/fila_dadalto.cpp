/****************************************************************************
 * Arthur Pratti Dadalto
 * OBI 2015 - Fila
 * BIT, Segment Tree, busca binaria em BIT e Segment Tree em tempo logaritmico
 ***************************************************************************/

#include <stdio.h>

#define left(i) ((i) << 1)
#define right(i) (((i) << 1)+1)

const int MAXN = (1 << 21);

int max(int a, int b) { return (a > b) ? a : b; }

int h[MAXN];
int t[MAXN], p[MAXN], x[MAXN];
int bit[MAXN];
int ocup[MAXN];
int val[2*MAXN];

void update(int id, int l, int r, int a, int b)
{
	if(l == r)
		val[id] = b;
	else
	{
		int mid = (l+r)/2;
		if(a <= mid)
			update(left(id), l, mid, a, b);
		else
			update(right(id), mid+1, r, a, b);
		val[id] = max(val[left(id)], val[right(id)]);
	}
}

int query(int id, int l, int r, int a, int b, int c)
{
	if(val[id] <= c)
		return 0;
	if(a == l && b == r)
	{
		int mid = (l+r)/2;

		if(l == r)
			return l;
		if(val[right(id)] > c)
			return query(right(id), mid+1, r, mid+1, b, c);
		else
			return query(left(id), l, mid, a, mid, c);
	}
	else
	{
		int mid = (l+r)/2;
		if(b <= mid)
			return query(left(id), l, mid, a, b, c);
		else if(a > mid)
			return query(right(id), mid+1, r, a, b, c);
		else
		{
			int tmp = query(right(id), mid+1, r, mid+1, b, c);
			if(tmp == 0)
				return query(left(id), l, mid, a, mid, c);
			else
				return tmp;
		}
	}
}

int find(int y)
{
	int retv = 0;
	for(int i = 20; i >= 0; i--)
		if(bit[retv + (1 << i)] <= y)
			y -= bit[retv + (1 << i)], retv = retv + (1 << i);
	return (y == 0) ? retv : -1;
}

void change(int pos, int y)
{
	for(int i = pos; i < MAXN; i += -i&i)
		bit[i] += y;
}

int get(int pos)
{
	int retv = 0;
	for(int i = pos; i > 0; i -= -i&i)
		retv += bit[i];
	return retv;
}

int
main(void)
{
	int n, q;
	scanf("%d", &n);
	for(int i = 0; i < n; t[i] = 0, p[i] = i, i++)
		scanf("%d", &x[i]);
	scanf("%d", &q);
	for(int i = n; i < n + q; i++)
		scanf("%d %d %d", &t[i], &p[i], &x[i]);
	for(int i = 1; i <= n+q; ocup[i] = 1, i++)
		change(i, 1);

	for(int i = n+q-1; i >= 0; i--)
	{
		if(t[i] == 0)
		{
			p[i] = find(p[i]) + 1;
			change(p[i], -1);
			ocup[p[i]] = 0;
		}
		else
		{
			p[i] = find(p[i] - 1) + 1;
		}
	}

	for(int i = 0; i < n + q; i++)
	{
		if(t[i] == 0)
		{
			update(1, 1, n+q, p[i], x[i]);
			change(p[i], 1);
			h[p[i]] = x[i];
		}
		else
		{
			printf("%d\n", get(query(1, 1, n+q, 1, p[i], h[p[i]] + x[i])));
		}
	}

}