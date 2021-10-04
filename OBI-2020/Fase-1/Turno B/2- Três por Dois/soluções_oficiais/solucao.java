// OBI2020
// camisetas
import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class solucao {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int n = in.nextInt();
	Integer[] preco = new Integer[n];
	long sol = 0;
	
	for (int i=0; i<n; i++)
	    preco[i] = in.nextInt();
	Arrays.sort(preco, Collections.reverseOrder());

	for (int i=0; i<n; i++) {
	    if (i % 3 == 2) {
		continue;
	    }
	    sol += preco[i];
	}
	System.out.println(sol);
    }
}
