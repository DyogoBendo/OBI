// Guilherme A. Pinto, OBI-2017, codigo

import java.util.*;
import java.io.*;
import java.lang.*;

public class codigo_java {

    public static int MAX = 10;
    
    public static void main(String[] args) throws IOException {
	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int N;
	String buf;

	ArrayList<HashSet<String>> prefixo = new ArrayList<HashSet<String>>(MAX+1);
	ArrayList<HashSet<String>> sufixo = new ArrayList<HashSet<String>>(MAX+1);

	for ( int i = 0; i <= MAX; i++ ){
	    prefixo.add(new HashSet<String>());
	    sufixo.add(new HashSet<String>());
	}
	
        String line = in.readLine();    
        StringTokenizer tokenizer = new StringTokenizer(line," ");
        N = Integer.parseInt(tokenizer.nextToken());

	for ( int i = 0; i < N; i++ ){
	    line = in.readLine();
	    tokenizer = new StringTokenizer(line," ");
	    buf = tokenizer.nextToken();

	    // checa validade
	    for ( int k = MAX; k > 0; k-- ){
		String pref = buf.substring(0,k);
		if ( sufixo.get(k).contains( pref ) ){
		    if ( k == MAX ){
			System.out.println( buf );
			return;
		    } else {
			String suf = buf.substring(k,MAX);
			if ( prefixo.get(MAX-k).contains( suf ) ){
			    System.out.println( buf );
			    return;
			}
		    }
		}
	    }

	    // inclui palavra (prefixos e sufixos)
	    for ( int k = MAX; k >= 0; k-- ){
		if ( k < MAX && k > 0 ){
		    String pref = buf.substring(0,k);
		    prefixo.get(k).add( pref );
		}
		if ( k < MAX ){
		    String suf = buf.substring(k,MAX);
		    sufixo.get(MAX-k).add( suf );
		}
	    }
	    
	}

	System.out.println( "ok" );
    }
}
