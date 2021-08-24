#include <cstdio>
#include <set>
using namespace std;

int main(){
	set<int> s;
	s.clear();
	int N;
	scanf("%d", &N);
	for(int i = 0; i < N;i++){
		int valor;
		scanf("%d", &valor);
		s.insert(valor);
	}
	printf("%d\n", (int)s.size());
	return 0;
}
