// Simulador - F2P2 - OBI 2009
// Rogério Júnior
// Complexidade: O(m^2)

#include "bits/stdc++.h"

using namespace std;

#define F first
#define S second
#define PB push_back

typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef long long ll;

int mod(int x){
	
	if(x>0) return x;
	return -x;
}

int n, m;

vector<iii> query;
vector<ii> interv;

void cut(int a){
	
	if(a>=n or a<=0) return;
	
	int sum=0, id;
	
	for(int i=0;i<interv.size();i++){
		
		int qtd=mod(interv[i].F-interv[i].S)+1;
		
		if(sum+qtd>a){
			
			id=i;
			break;
		}
		
		sum+=qtd;
	}
	
	int mid;
	
	a-=sum;
	
	if(!a) return;
	
	ii novo;
	
	if(interv[id].F<=interv[id].S){
		
		mid=interv[id].F+a;
		
		novo=ii(mid,interv[id].S);
		interv[id].S=mid-1;
	}
	
	else{
		
		mid=interv[id].F-a;
		
		novo=ii(mid,interv[id].S);
		interv[id].S=mid+1;
	}
	
	interv.PB(novo);
	
	for(int i=interv.size()-1;i>id+1;i--) swap(interv[i],interv[i-1]);
}

ll soma(int a, int b){
	
	int sum=0;
	
	ll resp=0;
	
	for(int i=0;i<interv.size();i++){
		
		int qtd=mod(interv[i].F-interv[i].S)+1;
		
		if(sum+qtd>=a and sum+qtd<=b) resp+=(ll(interv[i].F+interv[i].S)*ll(qtd))/2LL;
		
		sum+=qtd;
	}
	
	return resp;
}

void inverte(int a, int b){
	
	int sum=0, ini, fim;
	
	for(int i=0;i<interv.size();i++){
		
		if(sum==a-1) ini=i;
		
		int qtd=mod(interv[i].F-interv[i].S)+1;
		
		if(sum+qtd==b) fim=i;
		
		sum+=qtd;
	}
	
	for(int i=ini;i<=(ini+fim)/2;i++) swap(interv[i],interv[fim-(i-ini)]);
	
	for(int i=ini;i<=fim;i++) swap(interv[i].F,interv[i].S);
}

int main(){
	
	cin >> n >> m;
	
	interv.PB(ii(1,n));
	
	for(int i=0;i<m;i++){
		
		char op;
		int a, b;
		
		cin >> op >> a >> b;
		
		cut(a-1), cut(b);
		
		if(op=='S') cout << soma(a,b) << "\n";
		if(op=='I') inverte(a,b);
	}
	
	return 0;
}