// OBI-2019, etiquetas

import java.util.*;
import java.io.*;
import java.lang.*;

public class etiquetas_java {

  public static int INF = 1000000000; // 10^9 >> 10000^2

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter writer = new PrintWriter(System.out);

    String line = in.readLine();
    StringTokenizer tokenizer = new StringTokenizer(line," ");
    int N = Integer.parseInt(tokenizer.nextToken());
    int K = Integer.parseInt(tokenizer.nextToken());
    int C = Integer.parseInt(tokenizer.nextToken());

    int f[] = new int[N+1];

    int m[][] = new int[K+1][N+1];
    for ( int i = 0; i <= K; i++ )
      for ( int j = 0; j <= N; j++ )
        m[i][j] = -INF;

    line = in.readLine();
    tokenizer = new StringTokenizer(line," ");

    m[0][0] = 0;
    for( int i = 1; i <= N; i++ ){
      f[i] = Integer.parseInt(tokenizer.nextToken());
      m[0][i] = m[0][i-1]+f[i];
    }

    // DP
    for( int k = 1; k <= K; k++ )
      for( int i = k*C; i <= N; i++ )
        m[k][i] = Math.max( m[k-1][i-C], m[k][i-1]+f[i] );

    writer.println( m[K][N] );
    writer.close();
  }
}
