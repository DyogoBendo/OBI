// OBI2020 - Fase 2
// estrada

import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class solucao {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int t = in.nextInt();
	int n = in.nextInt();
	Integer[] cidades = new Integer[n];
	int compr_oeste = 0;
	int compr_leste = 0;
	int dif_oeste, dif_leste;
	double compr, compr_min;
  
	for (int i=0; i<n; i++) 
	    cidades[i] = in.nextInt();
	Arrays.sort(cidades);

	// inicia com a extensao do primeiro trecho a oeste
	compr_min = cidades[0] + (cidades[1] - cidades[0])/2.0;
	for (int i=1; i<n-1; i++) {
	    dif_oeste = cidades[i] - cidades[i-1];
	    dif_leste = cidades[i+1] - cidades[i];
	    compr = dif_oeste/2.0 + dif_leste/2.0;
	    if (compr < compr_min)
		compr_min = compr;
	}
	
	// extensao do ultimo trecho a leste
	compr = (cidades[n-1] - cidades[n-2])/2.0 + (t - cidades[n-1]);
	if (compr < compr_min)
	    compr_min = compr;
	
	System.out.printf("%.2f\n", compr_min);
    }
}
