// OBI2020 - Fase 2
// quebra

import java.util.Scanner;
import java.util.Arrays;

public class solucao {
    public static final int MAX = 200;
    public static boolean[] visitado = new boolean[MAX];
    public static boolean[][] adj = new boolean[MAX][MAX];
    public static int alcancados = 0;
    public static int S;
    
    public static void busca(int k) {
	if (!visitado[k]) {
	    alcancados++;
	    visitado[k] = true;
	    for (int q = 0; q < S; q++) {
		if (adj[k][q])
		    busca(q);
	    }
	}
    }
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int[] altura = new int[MAX];
	int i, a, b;

	S = in.nextInt();
	int T = in.nextInt();
	int P = in.nextInt();
	for(i=0; i<S; i++)
	    altura[i] = in.nextInt();
	for (i=0; i<T; i++) {
	    a = in.nextInt();
	    b = in.nextInt();
	    a--; b--;
	    if (altura[a] > altura[b])
		adj[a][b] = true;
	    else if (altura[a] < altura[b])
		adj[b][a] = true;
	}

	busca(P-1);
	System.out.println(alcancados-1);
    }
}

