// OBI2020 - Fase 3
// rede social

import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class solucao {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int n = in.nextInt();
	Integer[] repostagens = new Integer[n];
  
	for (int i=0; i<n; i++) 
	    repostagens[i] = in.nextInt();

	// ordena do maior para o menor
	Arrays.sort(repostagens, Collections.reverseOrder());

	// calcula o fator de influencia
	int fi = 0;
	while (fi < n && repostagens[fi] >= fi + 1)
	    fi++;
	
	System.out.printf("%d\n", fi);
    }
}
