// Guilherme A. Pinto, OBI-2017, imperio

import java.util.*;
import java.io.*;
import java.lang.*;

public class imperio_java {

    public static int N,res;
    public static ArrayList<ArrayList<Integer>> g;
    
    public static int dfs( int i, int pai ){
	int peso = 1;
	
	for ( int p: g.get(i) )
	    if ( p != pai )
		peso += dfs( p, i );
	
	int dif = Math.abs(N-2*peso);
	if ( dif < res ) res = dif;
	
	return peso;
    }
    
    
    public static void main(String[] args) throws IOException {
	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        String line = in.readLine();    
        StringTokenizer tokenizer = new StringTokenizer(line," ");
        N = Integer.parseInt(tokenizer.nextToken());
	
	g = new ArrayList<ArrayList<Integer>>(N+1);

	for ( int i = 0; i <= N; i++ )
	    g.add(new ArrayList<Integer>());

	
	for ( int i = 1; i <= N-1; i++ ){
	    line = in.readLine();
	    tokenizer = new StringTokenizer(line," ");
	    int A = Integer.parseInt(tokenizer.nextToken());
	    int B = Integer.parseInt(tokenizer.nextToken());
	    g.get(A).add(B);
	    g.get(B).add(A);
	}

	res = N;
	dfs( 1, -1 );

	System.out.println( res );
    }
}
