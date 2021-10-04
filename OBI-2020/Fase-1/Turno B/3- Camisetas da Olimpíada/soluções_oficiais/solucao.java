// OBI2020
// camisetas
import java.util.Scanner;

public class solucao {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int n = in.nextInt();
	int[] prefs = new int[n];	
	for (int i=0; i<n; i++)
	    prefs[i] = in.nextInt();
	int prod_p = in.nextInt();
	int prod_m = in.nextInt();

	for (int i=0; i<n; i++) {
	    if (prefs[i] == 1)
		--prod_p;
	    else
		--prod_m;
	}
	if (prod_p >= 0 && prod_m >= 0)
	    System.out.println("S");
	else
	    System.out.println("N");
    }
}
