/*
 * Lencol
 * R. Anido
 */

import java.io.*;
import java.util.*;

class lencol {

    static boolean test(int a,int b,int x,int y) {
	if(a<=x && b<=y)	return true;
	if(a<=y && b<=x)	return true;
	return false;
    }
    

    public static void main(String[] arg) {
	Scanner s = new Scanner(new BufferedReader (new InputStreamReader(System.in)));
	int h1,b1;
	int h2,b2;
	int h,b;
	//verificador
	int ver=0;

	h1=s.nextInt();
	b1=s.nextInt();
	h2=s.nextInt();
	b2=s.nextInt();
	b=s.nextInt();
	h=s.nextInt();

	//verificando se o retangulo de lados h e b 
	//cabe dentro do retangulo de lados h1 e b1
	
	if(test(h,b,h1,b1))	ver=1;
	
	//verificando se o retangulo de lados h e b 
	//cabe dentro do retangulo de lados h1 e b1
	
	if(test(h,b,h2,b2))	ver=1;
	
	for(int i=0;i<=h;i++)
	{
		//costura paralela ao lado b e separando o 
		//lado h em i e h-i
		if(test(b,i,h1,b1)&&test(b,h-i,h2,b2)) ver=1;
		if(test(b,i,h2,b2)&&test(b,h-i,h1,b1)) ver=1;
	}
	for(int i=0;i<=b;i++)
	{
		//costura paralela ao lado h e separando o 
		//lado b em i e b-i
		if(test(h,i,h1,b1)&&test(h,b-i,h2,b2)) ver=1;
		if(test(h,i,h2,b2)&&test(h,b-i,h1,b1)) ver=1;
	}
	
	if (ver==1) System.out.println("S");
	else System.out.println("N");

    }
}


