// OBI-2019, exploracao

import java.util.*;
import java.io.*;
import java.lang.*;

public class leal_java {

  public static class Pair { 
    int first,second;

    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }
  }

  public static class Ordena implements Comparator<Pair> {
    public int compare(Pair a, Pair b) { return a.first - b.first; }
  }

  public static final int N = 500010;
  public static int n;
  public static Long P, Q, ans;
  public static Long[] bit;

  public static ArrayList<Pair> v;
  public static TreeSet<Long> comp;

  public static void upd(int x, Long v)
  {
    for(int i = x; i < N; i += (i&-i)) bit[i] += v;
  }

  public static Long query(int x)
  {
    Long sum = 0L;
    for(int i = x; i > 0; i -= (i&-i)) sum += bit[i];
    return sum;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter writer = new PrintWriter(System.out);
  
    String line = in.readLine();
    StringTokenizer tokenizer = new StringTokenizer(line," ");
    n = Integer.parseInt(tokenizer.nextToken());
    P = Long.parseLong(tokenizer.nextToken());
    Q = Long.parseLong(tokenizer.nextToken());

    if(Q < 0L)
    {
      P *= -1L;
      Q *= -1L;
    }

    v = new ArrayList<Pair>(n+1);
    v.add( new Pair(0,0) ); // sentinela

    comp = new TreeSet<Long>();

    for(int i = 1; i <= n; i++)
    {
      line = in.readLine();
      tokenizer = new StringTokenizer(line," ");
      int f = Integer.parseInt(tokenizer.nextToken());
      int s = Integer.parseInt(tokenizer.nextToken());

      v.add( new Pair(f,s) );

      Long k = Q*s - P*f;

      comp.add(k);
    }

    Ordena pc = new Ordena();
    Collections.sort(v, pc);

    ArrayList<Long> c = new ArrayList<Long>(comp);
    int cn = c.size();

    bit = new Long[N];
    for(int i = 0; i < N; i++) bit[i] = 0L;
    ans = 0L;

    for(int i = 1; i <= n; i++)
    {
      Long k = Q*v.get(i).second - P*v.get(i).first;

      int l = Collections.binarySearch(c, k);
      l++;

      ans += query(l);

      upd(l, 1L);
    }

    writer.println( ans );
    writer.close();
  }
}
