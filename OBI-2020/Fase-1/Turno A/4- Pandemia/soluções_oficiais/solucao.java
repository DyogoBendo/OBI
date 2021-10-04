// OBI-2020, pandemia

import java.util.*;
import java.io.*;
import java.lang.*;

public class solucao {

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter writer = new PrintWriter(System.out);
  
    String line = in.readLine();
    StringTokenizer tokenizer = new StringTokenizer(line," ");
    int N = Integer.parseInt(tokenizer.nextToken());
    int M = Integer.parseInt(tokenizer.nextToken());

    line = in.readLine();
    tokenizer = new StringTokenizer(line," ");
    int I = Integer.parseInt(tokenizer.nextToken());
    int R = Integer.parseInt(tokenizer.nextToken());

    boolean amigo[] = new boolean[N+1];
    for( int i = 0; i <= N; i++ )
        amigo[i] = false;

    for( int m = 1; m <= M; m++ ){

      // amigo I participou infectado (de fora)
      if ( m == R ) amigo[I] = true;

      // le lista de amigos na reuniao
      ArrayList<Integer> presentes = new ArrayList<Integer>();

      line = in.readLine();
      tokenizer = new StringTokenizer(line," ");

      int A = Integer.parseInt(tokenizer.nextToken());
      boolean participanteInfectado = false;

      for( int a = 1; a <= A; a++ ){
        int k = Integer.parseInt(tokenizer.nextToken());
        presentes.add( k );
        if ( amigo[k] ) participanteInfectado = true;
      }

      // contaminacao
      if ( participanteInfectado )
        for( int a: presentes )
          amigo[a] = true;
    }

    // conta infectados ao final
    int cnt = 0;
    for ( boolean infectado: amigo )
      if ( infectado )
        cnt++;

    writer.println( cnt );
    writer.close();
  }
}
