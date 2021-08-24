#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
    int n, v[3], i;
    
    scanf("%d", &n);
    
    for (i=0; i<3; i++)
    {
        scanf("%d", &v[i]);
    }
    
    sort(v, v+3);
    
    i = 0;
    while (i < 3 && v[i] <= n)
    {
        n -= v[i];
        i++;
    }
    printf("%d\n", i);
    
}