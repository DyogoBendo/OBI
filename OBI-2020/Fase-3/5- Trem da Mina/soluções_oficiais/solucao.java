// Guilherme A. Pinto

import java.util.Scanner;
import java.io.*;
import java.lang.*;

public class solucao {

    static int MAXG = 100;
    static int INF  = 1000000000;
    static int MAXS = 100000;
    static int MAXQ = 100;
    static int MAXT = 200000; // 2*MAXS

    public static class estacao {
	public int[] e;
	public int m,d,h,hi,pai,w_ciclo,ne;
	public estacao(){ e = new int[MAXG];}
    }

    public static class trilho { public int u,v,w; }

    static estacao[] s;
    static trilho[] t;
    static int S,T,Q,X,M,count;

    ////////// Minheap for Dijkstra /////////////

    public static int L( int i ){ return i<<1; }
    public static int R( int i ){ return (i<<1)|1; }
    public static int F( int i ){ return i>>1; }

    static int hS;
    static int[] H;

    public static void heapInsertUpdate( int id ){
	int i = s[id].hi;
	if ( i == -1 ) i = ++hS;
	while ( i > 1 && s[H[F(i)]].h > s[id].h ){
	    H[i] = H[F(i)]; s[H[F(i)]].hi = i; i = F(i);
	}
	H[i] = id; s[id].hi = i;
    }
    public static void heapify( int i ){
	int sm,aux,l = L(i),r = R(i); sm = i;
	if ( l <= hS && s[H[l]].h < s[H[sm]].h ) sm = l;
	if ( r <= hS && s[H[r]].h < s[H[sm]].h ) sm = r;
	if ( sm != i ){
	    aux = H[i];
	    H[i] = H[sm]; s[H[sm]].hi = i;
	    H[sm] = aux; s[aux].hi = sm;
	    heapify( sm );
	}
    }
    public static int heapExtractMin(){
	int min = H[1];
	H[1] = H[hS]; s[H[hS--]].hi = 1; heapify( 1 );
	return min;
    }

    ///////////////////////////////////////////

    public static int get( int i, int k ){
	int u = t[s[i].e[k]].u;
	int v = t[s[i].e[k]].v;
	if ( u == i ) return v;
	return u;
    }
    
    public static int pesoTrilho( int a, int b ){
	int k,j,val = 0;
	for ( k = 0; k < s[a].ne; k++ ){
	    j = s[a].e[k];
	    if ( t[j].u == b || t[j].v == b ){
		val = t[j].w; break;
	    }
	}
	return val;
    }

    public static void processaCiclo( int j, int i ){
	int k,w;
	w = 0; k = i;
	while ( s[k].pai != j ){
	    w += pesoTrilho( k, s[k].pai );
	    k = s[k].pai;
	}
	w += pesoTrilho( k, j );
	w += pesoTrilho( j, i );
	/* anota peso em cada vertice */
	k = i;
	while ( s[k].pai != j ){
	    s[k].w_ciclo = w;
	    s[k].m = 2;
	    k = s[k].pai;
	}
	s[k].w_ciclo = w; s[k].m = 2;
	s[j].w_ciclo = w; s[j].m = 2;
    }
    
    public static void dfs( int i ){
	int k,j;
	
	for ( k = 0; k < s[i].ne; k++ ){
	    j = get( i, k );
	    if ( s[j].m == 0 ){
		s[j].m = 1; 
		s[j].pai = i; 
		dfs( j );
	    } else {
		if ( s[j].m == 1 ){
		    /* se vizinho nao eh o pai, achou ciclo */
		    if ( j != s[i].pai ) processaCiclo( j, i );
		}
	    }
	}
    }
    
    public static int dijkstra( int X ){
	int i,j,k,c,val,min = INF;
	
	hS = 0; s[X].h = 0;
	heapInsertUpdate( X );
	
	while( hS > 0 ){
	    i = heapExtractMin();
	    
	    /* corte para otimizar */
	    if ( min <= (2*s[i].h) + M ) return min;
	    
	    /* testa se trem cabe no ciclo */
	    if ( s[i].w_ciclo >= M ){
		val = (2*s[i].h) + s[i].w_ciclo;
		if ( val < min ) min = val;
	    }
	    
	    for ( k = 0; k < s[i].ne; k++ ){
		j = get( i, k );
		c = t[s[i].e[k]].w;
		if ( s[j].h > s[i].h + c ){
		    s[j].h = s[i].h + c;
		    heapInsertUpdate( j );
		}
	    }
	}    
	
	if ( min < INF ) return min;
	return -1;
    }
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	int i,j,k,a,b,c,min;

	S = in.nextInt(); T = in.nextInt();

	H = new int[MAXS+1];
	s = new estacao[MAXS+1];
	for ( i = 0; i <= S; i++ ) s[i] = new estacao();
	t = new trilho[MAXT+1];
	for ( i = 0; i <= T; i++ ) t[i] = new trilho();

	/* monta o grafo */
	for ( i = 1; i <= S; i++ ){
	    s[i].m = s[i].d = s[i].ne = s[i].w_ciclo = 0;
	    s[i].pai = -1;
	}
	for ( i = 0; i < T; i++ ){
	    a = in.nextInt(); b = in.nextInt(); c = in.nextInt();
	    t[i].u = a; t[i].v = b; t[i].w = c;
	    s[a].e[s[a].ne++] = i;
	    s[b].e[s[b].ne++] = i;
	}

	/* calcula peso de cada ciclo, anotando nas estacoes */
	for ( i = 1; i <= S; i++ ) 
	    if ( s[i].m == 0 ){
		s[i].m = 1; dfs( i );
	    }

	Q = in.nextInt();

	while( Q > 0 ){
	    X = in.nextInt(); M = in.nextInt();
	    
	    /* limpa cotas para dijkstra */
	    for ( i = 1; i <= S; i++ ){
		s[i].h = INF; s[i].hi = -1;
	    }
	    
	    System.out.print(String.format("%d\n",dijkstra( X )));
	    
	    Q--;
	}	
    }
}
