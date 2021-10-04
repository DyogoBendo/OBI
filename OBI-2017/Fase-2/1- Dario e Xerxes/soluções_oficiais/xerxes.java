// r. anido
// problema xerxes, OBI2017

import java.util.Scanner;

public class xerxes {
    
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in); 
	int d,x;               // apostas de dario e xerxes
	int nd=0,nx=0;         // número total de partidas ganhas por dario e xerxes
	int n = in.nextInt();  // número de partidas

	for (int i=0; i<n; i++) {
	    // lê as duas apostas
	    d = in.nextInt();
	    x = in.nextInt();
	    if (x==0)
		x = 5;
	    if (d<x) {
		if ((x-d)<=2)
		    nd++;              // dario ganha a partida
		else
		    nx++;              // xerxes ganha a partida
	    }
	    else if ((d-x)<=2)
		nx++;                  // xerxes ganha a partida
	    else
		nd++;                  // dario ganha a partida
	}
	if (nd>nx)
	    System.out.println("dario");   // dario ganha o jogo
	else
	    System.out.println("xerxes");  // xerxes ganha o jogo
    }
}
