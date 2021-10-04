// r. anido
// problema frete, OBI2017

import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

class Vertice {
    public int ident,custoFrete;
    public List<Aresta> arestas=new ArrayList<Aresta>();
    public Vertice(int id) {
    	this.ident=id;
	custoFrete=Integer.MAX_VALUE;
    }
    public void adicionaAresta(Vertice v, int custo) {
	Aresta a=new Aresta(v, custo);
	arestas.add(a);
    }
}

class Aresta {
    public Vertice destino;
    public int custo;
    public Aresta(Vertice v, int custo) {
        this.destino = v;
        this.custo = custo;
    }
}

class comparaCusto implements Comparator<Vertice> {
	public int compare(Vertice a, Vertice b) {
	    return a.custoFrete - b.custoFrete;
	}
}

public class frete {
    public static final int MAX=Integer.MAX_VALUE;
    public static int N,M;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); 
	int x,y,c;

	N = in.nextInt();
	M = in.nextInt();
	Vertice mapa[] = new Vertice[N];
	for (int i=0; i<N; i++)
	    mapa[i]=new Vertice(i);
	mapa[0].custoFrete=0;
	for (int i=0; i<M; i++) {
	    x = in.nextInt()-1;
	    y = in.nextInt()-1;
	    c = in.nextInt();
	    mapa[x].adicionaAresta(mapa[y],c);
	    mapa[y].adicionaAresta(mapa[x],c);
	}

	// algoritmo de Dijkstra para encontrar o caminho de menor custo
	Queue<Vertice> filaPrioridade = new PriorityQueue<>(N, new comparaCusto());
	filaPrioridade.add(mapa[0]);  // insere (cidade=0, custo=0)
	Vertice u,v;
	while (!filaPrioridade.isEmpty()) { 
	    u = filaPrioridade.poll();
	    for (Aresta a: u.arestas) {
		v = a.destino;
		int alternativa = u.custoFrete + a.custo;
		if (alternativa < v.custoFrete) {
		    filaPrioridade.remove(v);
		    v.custoFrete = alternativa;
		    filaPrioridade.add(v);
		}
	    }
	}
	// imprime o resultado para cidade N-1
	System.out.println(mapa[N-1].custoFrete);
    }
}
