// OBI-2020, fissura

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

  public static int[] di = {1,0,-1,0};
  public static int[] dj = {0,1,0,-1};
  public static int N,F;

  public static Queue<Pair> q;
  public static ArrayList<ArrayList<Character>> m;

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter writer = new PrintWriter(System.out);
  
    String line = in.readLine();
    StringTokenizer tokenizer = new StringTokenizer(line," ");
    N = Integer.parseInt(tokenizer.nextToken());
    F = Integer.parseInt(tokenizer.nextToken());

    m = new ArrayList<ArrayList<Character>>();
    for( int i = 0; i < N; i++ ) m.add( new ArrayList<Character>() );

    // input
    for( int i = 0; i < N; i++ ){
      line = in.readLine();
      tokenizer = new StringTokenizer(line," ");
      String l = tokenizer.nextToken();
      for ( int j = 0; j < N; j++ )
        m.get(i).add( l.charAt(j) );
    }

    q = new LinkedList<Pair>();

    if ( Character.digit(m.get(0).get(0),10) <= F ){

      m.get(0).set(0,'*');
      q.add( new Pair(0,0) );

      // BFS
      while( !q.isEmpty() ){
        Pair e = q.remove();

        int i = e.first;
        int j = e.second;

        for( int k = 0; k < 4; k++ ){
          int a = i+di[k];
          int b = j+dj[k];
          if ( a >= 0 && a < N && b >= 0 && b < N )
            if ( m.get(a).get(b) != '*' && Character.digit(m.get(a).get(b),10) <= F ){
              m.get(a).set(b,'*');
              q.add( new Pair(a,b) );
            }
        }
      }
    }

    // output
    for( ArrayList<Character> s: m ){
      for( int i = 0; i < N; i++ )
        writer.print( s.get(i) );
      writer.println();
    }

    writer.close();
  }
}
