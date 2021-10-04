// Guilherme A. Pinto, OBI-2017, arranhaceu

import java.util.*;
import java.io.*;
import java.lang.*;

public class arranhaceu_java {

    public static int N,Q;
    public static int bit[];
    public static int moradores[];
    
    public static void update( int x, int v ) {
	while (x <= N){
	    bit[x] += v;
	    x += x&-x;
	}
    }
    
    public static int query( int x ) {
	int r = 0;
	while( x > 0 ){
	    r += bit[x];
	    x -= x&-x;
	}
	return r;
    }
    
    public static void main(String[] args) throws IOException {
	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	PrintWriter writer = new PrintWriter(System.out);

        String line = in.readLine();    
        StringTokenizer tokenizer = new StringTokenizer(line," ");
        N = Integer.parseInt(tokenizer.nextToken());
        Q = Integer.parseInt(tokenizer.nextToken());

	bit = new int[N+1];
	moradores = new int[N+1];

	line = in.readLine(); tokenizer = new StringTokenizer(line," ");
	for ( int i = 1; i <= N; i++ ) {
            moradores[i] = Integer.parseInt(tokenizer.nextToken());
	    update( i, moradores[i] );
	}

	while ( Q-- > 0 ) {
	    int e,i,m,k;

	    line = in.readLine(); tokenizer = new StringTokenizer(line," ");
	    
	    e = Integer.parseInt(tokenizer.nextToken());
	    if ( e == 0 ) {
		i = Integer.parseInt(tokenizer.nextToken());
		m = Integer.parseInt(tokenizer.nextToken());
		int d = m - moradores[i];
		moradores[i] = m;
		update( i, d );
	    } else {
		k = Integer.parseInt(tokenizer.nextToken());
		writer.println( query(k) );
	    }
	}
	
	writer.close();
    }
}
