// r. anido
// problema papel, OBI2017

import java.util.*;
class Pair { //(int first, int second) {
    int first,second;

    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }
}

class Ordena implements Comparator<Pair> {
	public int compare(Pair a, Pair b) {
	    return a.first - b.first;
	}
}

public class papel {
    public static final int MAX=100000;
    public static int N;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); 
        int i,a,n,p=0;
	int last = 0;
	int max=1,nt=1;

	N = in.nextInt();
	Pair A[]=new Pair[N];
	int b[]=new int[N+2];

	b[0] = b[N+1] = 0;
	for(i = 1; i <= N; i++){
	    b[i] = 1;
	    a = in.nextInt();
	    A[i-1]=new Pair(a,i);
	}

	Arrays.sort(A, new Ordena());

	for (int e=0; e<N; e++ ){
	    a = A[e].first; i = A[e].second;
	    if (a != last) if ( nt > max ) max = nt;
	    b[i] = 0;
	    if (b[i-1]!=0 && b[i+1]!=0) nt++;
	    if (b[i-1]==0 && b[i+1]==0) nt--;
	}
  
	System.out.println(max+1);
    }
}
