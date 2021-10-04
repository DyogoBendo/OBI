// R. Anido
// chuva - OBI2019

import java.util.Scanner;

public class ranido_java {
    public static final int MAX = 500;
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int N = in.nextInt();
	int M = in.nextInt();
	String junk = in.nextLine(); // consome final de linha

	char[][] w = new char [N][MAX];

	for (int i = 0; i<N; i++) {
	    w[i] = (in.nextLine().toCharArray());
	}
  
	for (int i=0; i<N; i++) {
	    if (i > 0) {
		for (int j = 0; j < M; j++)
		    // de cima para baixo
		    if (w[i][j] == '.' && w[i-1][j] == 'o')
			w[i][j] = 'o';
	    }
	    if (i < N-1) {
		for(int j = M-2; j >= 0; j--)
		    // para a esquerda
		    if (w[i][j] == '.' && w[i][j+1] == 'o' &&
			 w[i+1][j+1] == '#')
			w[i][j] = 'o';
		for(int j = 1; j < M; j++)
		    // para a direita
		    if (w[i][j] == '.' && w[i][j-1] == 'o' &&
			 w[i+1][j-1] == '#')
			w[i][j] = 'o';
	    }
	}
	
	for (int i=0; i<N; i++)
	    System.out.println(new String(w[i]));
    }
}
