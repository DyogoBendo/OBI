// OBI-2019, metro

import java.util.*;
import java.io.*;
import java.lang.*;

public class metro_java {

  public static ArrayList<ArrayList<ArrayList<Integer>>> g;
  public static int[] d,c,pai;
  public static int N,M;

  // BFS
  public static int bfs( int i, ArrayList<ArrayList<Integer>> gf ){
    d = new int[gf.size()+1];
    pai = new int[gf.size()+1];

    for( int j = 0; j < gf.size()+1; j++ ) d[j] = pai[j] = -1;

    Queue<Integer> q = new LinkedList<Integer>();

    d[i] = 0;
    q.add( i );

    int v = i;

    while( !q.isEmpty() ){
      v = q.remove();
      for( int u: gf.get(v) )
        if ( d[u] == -1 ){
          d[u] = d[v] + 1;
          pai[u] = v;
          q.add( u );
        }
    }

    return v; // ultimo vertice a sair da fila
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter writer = new PrintWriter(System.out);
  
    String line = in.readLine();
    StringTokenizer tokenizer = new StringTokenizer(line," ");
    N = Integer.parseInt(tokenizer.nextToken());
    M = Integer.parseInt(tokenizer.nextToken());

    g = new ArrayList<ArrayList<ArrayList<Integer>>>();
    g.add( new ArrayList<ArrayList<Integer>>() );
    for( int i = 0; i < N+1; i++ ) g.get(0).add( new ArrayList<Integer>() );
    g.add( new ArrayList<ArrayList<Integer>>() );
    for( int i = 0; i < M+1; i++ ) g.get(1).add( new ArrayList<Integer>() );

    for( int k = 0; k < 2; k++ ){
      for( int i = 0; i < g.get(k).size()-2; i++ ){
        line = in.readLine();
        tokenizer = new StringTokenizer(line," ");
        int A = Integer.parseInt(tokenizer.nextToken());
        int B = Integer.parseInt(tokenizer.nextToken());

        g.get(k).get(A).add(B);
        g.get(k).get(B).add(A);
      }
    }

    int l;
    c = new int[2];

    for( int k = 0; k < 2; k++ ){
      // encontra um diametro no grafo
      l = bfs( bfs( 1, g.get(k) ), g.get(k) );

      // encontra o primeiro vertice central no diametro do grafo
      c[k] = l;
      while( d[c[k]] > d[l]/2 ) 
        c[k] = pai[c[k]];
    }

    writer.print( c[0] );
    writer.print( " " );
    writer.println( c[1] );
    writer.close();
  }
}
