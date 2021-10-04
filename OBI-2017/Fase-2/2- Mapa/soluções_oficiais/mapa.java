// r. anido
// problema mapa, OBI2017

import java.util.Scanner;

public class mapa {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); 
        int n,m;
	int pos_l=-1,pos_c=-1;               // posição de Hermione
        char mapa[][];

        n=in.nextInt();                      // lê valores do tamanho do mapa
        m=in.nextInt();                      
        mapa=new char[n+2][m+2];             // vamos usar uma matriz maior, com "bordas", para não
                                             // ter que se preocupar com índices inválidos
        for (int i=1; i<=n; i++) {           // lê os valores iniciais do mapa
	    String linha=in.next();
            for (int j=1; j<=m; j++) {
		mapa[i][j]=linha.charAt(j-1);
		if (mapa[i][j] == 'o') {     // marca posição inicial de Herminone
		    pos_l = i;
		    pos_c = j;
		}
	    }
	}
	while (true) {                       // segue Hermione, marcando a posição corrente como já usada com '.'
	    if (mapa[pos_l+1][pos_c]=='H') {
		    mapa[pos_l][pos_c]='x';
		    pos_l++;
                }
            else if (mapa[pos_l-1][pos_c]=='H') {
                    mapa[pos_l][pos_c]='x';
                    pos_l--;
                }
            else if (mapa[pos_l][pos_c+1]=='H') {
                    mapa[pos_l][pos_c]='x';
                    pos_c++;
                }
            else if (mapa[pos_l][pos_c-1]=='H') {
                    mapa[pos_l][pos_c]='x';
                    pos_c--;
                }
            else
                break;
        }

        System.out.println(pos_l+" "+pos_c);   // imprime a resposta
    }
}
