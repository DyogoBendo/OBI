#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main(){
	int A, B, C;
	scanf("%d%d%d", &A, &B, &C);
	int H, L;
	scanf("%d%d", &H, &L);
	if(H < L)
		swap(H, L);
	int X = min(A, min(B, C)); //menor dimensao
	int Y = min(max(A, B), min(max(A, C), max(B, C))); //segunda menor dimensão
	if(X <= L && Y <= H)
		printf("S\n");
	else
		printf("N\n");
	return 0;
}
