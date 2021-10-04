// OBI-2020, acelerador

import java.util.*;
import java.io.*;
import java.lang.*;

public class solucao {

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter writer = new PrintWriter(System.out);
  
    String line = in.readLine();
    StringTokenizer tokenizer = new StringTokenizer(line," ");
    int D = Integer.parseInt(tokenizer.nextToken());

    writer.println( (D-5)%8 );
    writer.close();
  }
}
