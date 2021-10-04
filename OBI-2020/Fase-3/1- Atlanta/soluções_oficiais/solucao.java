// OBI2020 - Fase 3
// atlanta

import java.util.Scanner;

public class solucao {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int larg, compr;
	int a = in.nextInt();
	int b = in.nextInt();
  
	for(int x = 1; x <= b; x++) {
	    if (b % x != 0)
		continue;
	    larg = b/x + 2;
	    compr = x + 2;
	    if (a == 2*(compr+larg) - 4) {
		System.out.printf("%d %d\n",compr,larg);
		return;
	    }
	}
	System.out.println("-1 -1");
    }
}
