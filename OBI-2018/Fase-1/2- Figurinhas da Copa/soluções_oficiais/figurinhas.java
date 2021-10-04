// R. Anido
// figurinhas - OBI2018

import java.util.Scanner;

public class figurinhas {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int n = in.nextInt();
	int c = in.nextInt();
	int m = in.nextInt();
	Boolean[] carimbadas =  new Boolean[n];
	Boolean[] ja_tem =  new Boolean[n];
	int x, num_carimbadas=0;
	
	// inicializa vetores
	for (int i = 0; i < n; i++) {
	    ja_tem[i] = false;
	    carimbadas[i] = false;
	}
	
	// marca e conta figurinhas carimbadas
	for (int i = 0; i < c; i++) {
	    x = in.nextInt() - 1;
	    if (carimbadas[x])
		continue;
	    carimbadas[x] = true;
	    num_carimbadas += 1;
	}

	// verifica figurinhas compradas e marca
	for (int i = 0; i < m; i++) {
	    x = in.nextInt() - 1;
	    if (carimbadas[x])
		ja_tem[x] = true;
	}
	
	int conta = 0;
	// conta figurinhas carimbadas que ja tem
	for (int i = 0; i < n; i++)
	    if (carimbadas[i] && ja_tem[i])
		conta += 1;
	    
	// calcula e escreve a resposta
	System.out.println(c - conta);
    }
}
