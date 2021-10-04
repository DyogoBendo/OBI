// OBI-2019, corrida

import java.util.*;
import java.io.*;
import java.lang.*;

public class good_java {

  public static final int MAX = 4*(200505);

  public static ArrayList<ArrayList<Integer>> adj;

  public static int[] idx = new int[MAX];
  public static int[] ridx = new int[MAX];
  public static boolean[] vis = new boolean[MAX];
  public static int n;
  public static boolean[] dfsTree = new boolean[MAX];

  public static int aux = 0;

  public static void build(int l , int r , int curr){
    int mid = (l+r)/2;
    if(l == r){
      idx[curr] = l;
      ridx[l] = curr;
      return ;
    }
    idx[curr] = n + (++aux);
    build(l,mid,2*curr);
    build(mid +1 , r, 2*curr + 1); 
    adj.get(idx[curr]).add(idx[2*curr]);
    adj.get(idx[curr]).add(idx[2*curr +1]);
  }
 
  public static class Node {
    public int u , L , R;
  }

  public static ArrayList<Node> v;
  public static int m , l , r, ansj = -2;

  public static void create(int i, int x, int y, int l, int r, int curr){
    int mid = (l+r)/2;
    if(l == x && r == y){
      adj.get(i).add(idx[curr]);
      return ;
    }
    if(y <= mid){
      create(i , x, y, l ,mid , 2*curr);
    }
    else if(x > mid){
      create(i , x, y, mid + 1 , r, 2*curr +1);
    }
    else{
      create(i , x, mid ,l , mid, 2*curr);
      create(i , mid + 1, y,  mid + 1 ,r , 2*curr + 1);
    }
  }

  public static boolean dfs(int x){
    vis[x] = true;
    dfsTree[x] = true;
    boolean p = false;
    for(int w : adj.get(x) ){
      if(vis[w] && dfsTree[w]){
        return true;
      }
      else if(!vis[w]){
        p |= dfs(w);
      }
    }
    dfsTree[x] = false;
    return p;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter writer = new PrintWriter(System.out);

    String line = in.readLine();
    StringTokenizer tokenizer = new StringTokenizer(line," ");
    n = Integer.parseInt(tokenizer.nextToken());
    m = Integer.parseInt(tokenizer.nextToken());

    v = new ArrayList<Node>(m);
    for(int i = 0; i < m; i++) v.add(new Node());

    adj = new ArrayList<ArrayList<Integer>>(MAX);
    for(int i = 0; i < MAX; i++) adj.add(new ArrayList<Integer>()); 

    for(int i = 0 ; i < m ; i ++){
      line = in.readLine();
      tokenizer = new StringTokenizer(line," ");
      v.get(i).u = Integer.parseInt(tokenizer.nextToken());
      v.get(i).L = Integer.parseInt(tokenizer.nextToken());
      v.get(i).R = Integer.parseInt(tokenizer.nextToken());
    }

    l = 0;
    r = m - 1;

    while(l<=r){
      for(int i = 0 ; i <= 4*(n + 400) ; i++){
        adj.get(i).clear();
        vis[i] = false;
        dfsTree[i] = false;
      } 
      aux = 0;  
      build( 1, n, 1 );
      int mid = (l+r)/2;
      for(int i = 0 ; i <= mid ; i ++){
        create( v.get(i).u, v.get(i).L, v.get(i).R, 1, n, 1 );
      }
      boolean ans = false;
      for(int i = 1 ; i <= n; i ++){
        if(!vis[i] && !ans){
          ans |= dfs(i);
        }
      }
      if(ans){
        ansj = mid;
        r = mid - 1;
      }
      else{
        l = mid + 1;
      }
    }

    writer.println( ansj + 1 );
    writer.close();
  }
}