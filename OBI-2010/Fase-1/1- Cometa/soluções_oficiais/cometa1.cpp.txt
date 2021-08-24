/*
 * Solução 1 do problema 'Cometa' (OBI 2010 - Nível 2, Fase 1) 
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
     * Podemos então ir verificando os anos seguintes ao ano da entrada, vendo
     * se algum se encaixa na descrição acima. Encontraremos um ano válido em
     * no máximo 76 tentativas.
     */

    int x;
    scanf("%d", &x);

    for(int i = x + 1; ; i++)
        if((i - 1986) % 76 == 0) {
            printf("%d\n", i);
            break;
        }
}
