// OBI-2020, promocao

import java.util.*;
import java.io.*;
import java.lang.*;

public class solucao {

  public static class Pair { 
    int first, second; 
    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }
  };

  public static class ReturnPair { 
    int max0, max1; 
    public ReturnPair(int a, int b) {
        this.max0 = a;
        this.max1 = b;
    }
  };

  public static ArrayList<ArrayList<Pair>> g;
  public static int opt;
  public static int N,M;

  // DFS
  public static ReturnPair dfs( int v, int parent ){
    ReturnPair r = new ReturnPair(0,0);

    for ( Pair u: g.get(v) )

      if ( u.first != parent ){
        ReturnPair ret = dfs( u.first, v );
        if ( u.second == 0 ) r.max0 = Math.max( r.max0, ret.max1 + 1 );
        else r.max1 = Math.max( r.max1, ret.max0 + 1 );
      }

    opt = Math.max( opt, r.max0 + r.max1 + 1 );
    return r;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter writer = new PrintWriter(System.out);
  
    String line = in.readLine();
    StringTokenizer tokenizer = new StringTokenizer(line," ");
    N = Integer.parseInt(tokenizer.nextToken());

    g = new ArrayList<ArrayList<Pair>>();
    for( int i = 0; i <= N; i++ ) g.add( new ArrayList<Pair>() );

    for( int i = 1; i <= N-1; i++ ){
      line = in.readLine();
      tokenizer = new StringTokenizer(line," ");
      int A = Integer.parseInt(tokenizer.nextToken());
      int B = Integer.parseInt(tokenizer.nextToken());
      int E = Integer.parseInt(tokenizer.nextToken());

      g.get(A).add( new Pair(B,E));
      g.get(B).add( new Pair(A,E));
    }

    opt = 0;
    dfs( 1 , -1 );

    writer.println( opt );
    writer.close();
  }
}
