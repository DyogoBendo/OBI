// OBI2019
// Tarefa Imperial

import java.util.*;

public class imperial_java2 {

    public static int N;
    public static int[] valores;

    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	Set<Integer> visto = new HashSet<Integer>();
	N = in.nextInt();
	valores = new int[N];
	
	for (int i = 0; i<N; i++)
	    valores[i] = in.nextInt();

	int res = 1;
	for (int i=0; i<N; i++) {
	    if (visto.contains(valores[i])) continue;
	    else visto.add(valores[i]);
	    for (int j=0; j<N; j++) {
		int atual = 0;
		int ultimo = -1;
		for (int k=0; k<N; k++) {
		    if ((valores[k] == valores[i] || valores[k] == valores[j]) && valores[k] != ultimo){
			atual++;
			ultimo = valores[k];
		    }
		}
		res = Math.max(res, atual);
	    }
	}
	System.out.println(res);
    }
}
