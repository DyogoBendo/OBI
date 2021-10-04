// OBI2019
// Tarefa Imperial

import java.util.*;

public class imperial_java {

    public static int N;
    public static int[] valores;

    public static int maior( int a, int b, int pos ){
	
	if (pos == N)
	    return 0;
	
	if (valores[pos] != a)
	    return maior(a, b, pos+1);
	else
	    return 1 + maior(b, a, pos+1);
    }
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	N = in.nextInt();
	valores = new int[N];
	
	for (int i = 0; i < N; i++)
	    valores[i] = in.nextInt();

	int res = 1;
	for (int i = 1; i <= N; i++) {
	    for (int j = 1; j <= N; j++)
		if (i != j) 
		    res = Math.max(res, maior(i, j, 0));
	}
	System.out.println(res);
    }
}
