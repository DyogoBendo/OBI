// OBI2020 - Fase 2
// quebra

import java.util.Scanner;
import java.util.Arrays;

public class solucao {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	final int MAX = 505;
	final int MIN = -1000000000;
	int[] linha0 = new int[MAX];
	int[] linha1 = new int[MAX];
	int[][][] tab = new int[2][MAX][MAX];


	int n = in.nextInt();
	int elem_linha0 = in.nextInt();
	for(int i=0; i<elem_linha0; i++)
	    linha0[i] = in.nextInt();
	int elem_linha1 = in.nextInt();
	for(int i=0; i<elem_linha1; i++)
	    linha1[i] = in.nextInt();

	// PD
	int uma = 1;
	int outra = 1 - uma;
	for (int i=0; i<=elem_linha0; i++)
	    for (int j=0; j<=elem_linha1; j++)
		tab[uma][i][j] = MIN;

	tab[uma][elem_linha0][elem_linha1] = 0;
	tab[outra][elem_linha0][elem_linha1] = 0;
	
	for (int k=0; k<n; k++) {
	    for (int i=elem_linha0; i>=0; i--) {
		for (int j=elem_linha1; j>=0; j--) {
		    if (i == elem_linha0 && j == elem_linha1)
			continue;
		    tab[outra][i][j] = MIN;
		    if (i < elem_linha0)
			tab[outra][i][j] = Math.max(tab[outra][i][j], tab[uma][i+1][j]);
		    if (j < elem_linha1)
			tab[outra][i][j] = Math.max(tab[outra][i][j], tab[uma][i][j+1]);
		    if (i < elem_linha0 && j < elem_linha1)
			tab[outra][i][j] = Math.max(tab[outra][i][j],linha0[i]*linha1[j] + tab[uma][i+1][j+1]);
		}
	    }
	    uma = 1 - uma;
	    outra = 1 - uma;
	}
	System.out.println(tab[uma][0][0]);
    }
}
