// R. Anido
// soma - OBI2019

import java.util.Scanner;

public class soma_java {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int MAX=500000;

	int N = in.nextInt();
	int K = in.nextInt();
	int[] o = new int[MAX];
	int[] q = new int[MAX+1];
	int[] z = new int[MAX+1];


	for (int i=0; i<N; i++) 
	    o[i] = in.nextInt();

  // remove zeros do vetor original o[] e cria vetor auxiliar z[]
  // contendo o numero de zeros a esquerda de cada nao-zero
  //
  // entrada, o[]: 2 0 1 1 0 0 8 4 1 3, produz:
  //
  //          q[]: 2 1 1 8 4 1 3
  //          z[]: 0 1 0 2 0 0 0 0
    
	int cnt = 0, k = 0;
  
	for (int i=0; i<N; i++)
	    if (o[i] == 0) cnt++;
	    else {
		q[k] = o[i];
		z[k++] = cnt;
		cnt = 0;
	    }
	z[k] = cnt;
	N = k;
	q[N] = 0; // sentinela

	Long count = 0L;
  
	if (K == 0) {
	    // sequencia de z[i] zeros possui combinacao de z[i]+1, 2 a 2, retangulos
	    for (int i=0; i<=N; i++) 
		count += (Long.valueOf(z[i]+1)*Long.valueOf(z[i]))/2;
	} else {
	    // dois ponteiros sobre o vetor de nao-zeros
	    int l = 0, r = 0; 
	    int soma = q[0]; 
	    while (r < N) {
		if (soma <= K) {
		    if (soma == K) {
			count += Long.valueOf(z[l]+1)*Long.valueOf(z[r+1]+1);
		    }
		    soma += q[++r]; // move ponteiro direito
		} else {
		    soma -= q[l++]; // move ponteiro esquerdo
		    if (l > r) {
			r = l;
			soma = q[r]; // reinicia janela
		    }
		}
	    }
	}  
	System.out.println(count);
    }
}
