/*
 * Solução 2 do problema 'Cometa' (OBI 2010 - Nível 2, Fase 1)
 *
 * Maurício de Lemos Rodrigues Collares Neto (<mauricioc@gmail.com>)
 */

#include <cstdio>

int main()
{
    /* O cometa passa em 1986, 1986 + 76, 1986 + 2*76, 1986 + 3*76... Subtraindo
     * 1986 desses números, vemos que todos eles são todos os múltiplos não-ne-
     * gativos de 76. 
     *
     * Precisamos então calcular a próxima vez que o cometa passa, ou seja,
     * o próximo número y > x tal que (y - 1986) é um múltiplo não-negativo de 
     * 76. Ser um múltiplo de 76 significa que (y - 1986) % 76 = 0. Agora, se
     * (x - 1986) % 76 = m, então (x - 1986 + (76 - m)) % 76 = (m + 76 - m) % 76
     * = 76 % 76 = 0, done podemos apenas somar (76 - m) à entrada para obter um
     * ano onde o cometa passa.

     * É claro que o ano obtido acima é o próximo ano que o cometa passará 
     * novamente se m != 0, pois nenhum ano menor é tal que (y - 1986) é múl-
     * tiplo de 76. Mas o procedimento também funciona para o caso em que m 
     * é zero, como pode-se verificar separadamente. */

    int x;
    scanf("%d", &x);

    int m = (x - 1986) % 76;
    printf("%d\n", x + (76 - m));
}
