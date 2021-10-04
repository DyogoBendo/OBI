// OBI2020
// fotografia

import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class solucao {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int[] foto = new int[2];
	int[] moldura = new int[2];

	int melhor_moldura = -1;
	int menor_area = 200 * 200;

	int x = in.nextInt();
	int y = in.nextInt();
	if (x > y) {
	    foto[0] = y; foto[1] = x;
	}
	else {
	    foto[0] = x; foto[1] = y;
	}
	int n = in.nextInt();
	int area = foto[0] * foto[1];
	for (int i=0; i<n; i++) {
	    x = in.nextInt();
	    y = in.nextInt();
	    if (x > y) {
		moldura[0] = y; moldura[1] = x;
	    }
	    else {
		moldura[0] = x; moldura[1] = y;
	    }
	    if (moldura[0] >= foto[0] && moldura[1] >= foto[1]) {
		// moldura serve
		if (moldura[0] * moldura[1] - area < menor_area) {
		    melhor_moldura = i+1;
		    menor_area = moldura[0] * moldura[1] - area;
		}
	    }
	}
	System.out.println(melhor_moldura);
    }
}
