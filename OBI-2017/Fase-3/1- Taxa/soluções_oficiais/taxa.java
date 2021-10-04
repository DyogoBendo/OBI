/*
 * Taxa
 * OBI2017
 * R. Anido
 */

import java.io.*;
import java.text.DecimalFormat;

public class taxa {
    static final int MAXSIZE = 1000;
    static final int MAXVAL = 10000000;
    static int val[] = new int[MAXSIZE];
    static int sum[][] = new int[2*MAXSIZE-1][2*MAXSIZE-1];
    static int cost[][] = new int[2*MAXSIZE-1][2*MAXSIZE-1];
    static StreamTokenizer st;

    static int max(int a, int b) {
	if (a >= b) 
	    return a;
	else
	    return b;
    }

    public static void main (String arg[]) throws Exception{
	int i, j, k, l, q, q1;
	int n;
	double v;
	DecimalFormat twoDecPlcFormatter = new DecimalFormat("0.00");

	st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
	try{st.nextToken();} catch (java.io.IOException e) {e.printStackTrace();}
	n = (int) st.nval;
	try{st.nextToken();} catch (java.io.IOException e) {e.printStackTrace();}
	v = (double) st.nval;
	for (i=0; i<n; i++) {
		try{st.nextToken();} catch (java.io.IOException e) {e.printStackTrace();}
		val[i] = (int) st.nval;
	}
	// pre-computa somas
	for (i=0; i<2*n - 1; i++)
	    sum[i][i] = val[i%n];
	for (j=1; j<2*n - 1; j++)
	    for (i=j-1; i>j-n && i >=0; i--) {
		sum[i][j] = sum[i+1][j] + sum[i][i];
	    }
	// inicializa tabela de custos
	for (i=0; i<2*n - 1; i++)
	    cost[i][i] = 0;
	for (i=0; i<2*n-2; i++) {
	    j = i + 1;
	    cost[i][j] = max(val[i % n], val[j % n]);
	}
	// computa todos os custos
	for (l=3; l<n+1; l++) {
	    for (i=0; i<2*n-l; i++) {
		j = i + l - 1;
		q = MAXVAL;
		for (k=i; k<j; k++) {
		    q1 = cost[i][k] + cost[k+1][j] + max(sum[i][k], sum[k+1][j]);
		    if (q1 < q)
			q = q1;
		}
		cost[i][j] = q;
	    }
	}
	// agora acha o minimo
	q = cost[0][n-1];
	for (i=1; i<n; i++) {
	    j = i + n -1;
	    if (cost[i][j] < q)
		q = cost[i][j];
	}
	// imprime o resitado
	System.out.println(twoDecPlcFormatter.format(v*q));
    }
}
