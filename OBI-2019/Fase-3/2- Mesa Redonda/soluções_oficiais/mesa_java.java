// OBI-2019, mesa

import java.util.*;
import java.io.*;
import java.lang.*;

public class mesa_java {

  public static int[] c = {0,0,0};

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter writer = new PrintWriter(System.out);

    String line = in.readLine();
    StringTokenizer tokenizer = new StringTokenizer(line," ");
    int A = Integer.parseInt(tokenizer.nextToken());    

    line = in.readLine();
    tokenizer = new StringTokenizer(line," ");
    int B = Integer.parseInt(tokenizer.nextToken());

    // Ana
    c[A%3] = 1;

    // Beatriz
    if ( c[B%3] == 1 ) {
      c[(B+1)%3] = 1;
    } else {
      c[B%3] = 1;
    }

    for ( int i = 0; i < 3; i++ )
      if ( c[i] == 0 )
        writer.println( i );

    writer.close();
  }
}
