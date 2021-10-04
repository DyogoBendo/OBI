// Guilherme A. Pinto, idade, OBI-2019

import java.util.Scanner;

public class idade_java {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	int M = in.nextInt();
	int A = in.nextInt();
	int B = in.nextInt();

	int C = M-A-B;
	
	int res = A;
	if ( res < B ) res = B;
	if ( res < C ) res = C;
	
	System.out.println(res);
    }
}
