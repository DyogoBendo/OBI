// R. Anido
// Piso - OBI2018

import java.util.Scanner;

public class piso {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int l = in.nextInt();
	int c = in.nextInt();

	// calcula 
	int t1 = l*c  + (l-1)*(c-1);
	int t2 = 2*(l-1) + 2*(c-1);

	// e escreve a resposta
	System.out.println(t1);
	System.out.println(t2);
    }
}
