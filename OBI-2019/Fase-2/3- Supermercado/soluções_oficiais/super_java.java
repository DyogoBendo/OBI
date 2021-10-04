// OBI-2019 Fase 2
// Problema Supermercado

import java.util.Scanner;

public class super_java {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int n;
	int g;               // gramas em cada supermercado
	double p,preco_grama; // preco em cada supermercado e menor preco conhecido por grama do produto
  
	n = in.nextInt();  
	preco_grama = 1000.0*1000; // máximo possível
	for (int i=0; i<n; i++) {
	    p = in.nextDouble();
	    g = in.nextInt();
	    if (p/g < preco_grama)
		preco_grama = p / g;
	}
	System.out.printf("%.2f\n",1000*preco_grama);
    }
}
