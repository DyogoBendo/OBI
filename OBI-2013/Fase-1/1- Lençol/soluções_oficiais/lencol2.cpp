#include <cstdio>
#include <algorithm>
using namespace std;

//b2,h2 esta contido em b1,h1?
bool contains(int b1,int h1,int b2,int h2) {
    return min(b1,h1) >= min(b2,h2) && max(b1,h1) >= max(b2,h2);
}

int main() {
    int r1[2],r2[2],r3[2];
    scanf("%d%d%d%d%d%d",&r1[0],&r1[1],&r2[0],&r2[1],&r3[0],&r3[1]);
    bool ok = 0;
    //verifica se a tarefa pode ser realizada recortando somente um dos retangulos
    if( contains(r1[0],r1[1],r3[0],r3[1]) || contains(r2[0],r2[1],r3[0],r3[1])) ok = 1;
    
    //itera por todas as disposicoes de retangulos
    for(int a=0;a<2;++a) {
        for(int b=0;b<2;++b) {
            int base = r1[a]+r2[b];
            int altura = min(r1[a^1],r2[b^1]);
            if(contains(base,altura,r3[0],r3[1])) ok = 1;
        }
    }
    printf("%c\n", ok ? 'S' : 'N');
    return 0;
}
