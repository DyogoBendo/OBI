// R. Anido
// Elevador - OBI2018

import java.util.Scanner;
import java.util.Arrays;

public class elevador_java {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int n = in.nextInt();
	int[] pesos = new int[n+1];

	pesos[0] = 0; // sentinela
  
	for (int i=1; i < n+1; i++)
	    pesos[i] = in.nextInt();

	Arrays.sort(pesos);

	char res = 'S';
  
	for (int i = 0; i < n; i++)
	    if (pesos[i+1] - pesos[i] > 8) {
		res = 'N';
		break;
	    }
	System.out.println(res);
    }
}
