#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1e5+10;

int v[MAXN];

int main() {
    int n,k;
    scanf("%d%d",&n,&k);
    for(int a=0;a<n;++a) scanf("%d",&v[a]);
    sort(v,v+n); //ordenando

    //passando por todas as possibilidades de escolha de k elementos das extremidades do vetor
    int best = v[n-1-k] - v[0];
    for(int a=1;a<=k;++a) best = min(best, v[n-1-k+a]-v[a]);
    printf("%d\n",best);
    return 0;
}
        
