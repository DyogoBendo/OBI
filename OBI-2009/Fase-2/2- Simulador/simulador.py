def cut(a):  # realiza um corte naquele valor
    global n, interv
    if a >= n or a<=0:  # corte é feito apenas se o valor estiver entre 1 e n - 1
        return
    sum=0  # soma das "distancias"

    id = 0
    for i in range(len(interv)):
        qtd = abs(interv[i][0] - interv[i][1]) + 1  
        # pegamos a diferença do intervalo, o que seria a "distancia"
        # por exemplo, no intervalo [7, 5] a distância é 3

        if qtd + sum > a:  # se adicionarmos essa distancia a soma, e ela for maior que "a"
            id = i  # definimos o identificador como i, e saimos do loop
            # estamos interessados apenas no primeiro valor em que a distância é maior que "a"
            break
        sum += qtd

    a -= sum  # "a" é subtraído pelas distâncias até chegar nele 
    if not a:  # se a soma das distâncias for igual a "a", então não há nada que possamos fazer
        return

    if interv[id][0] <= interv[id][1]:  # se o primeiro valor do intervalo for menor ou igual ao segundo
        mid = interv[id][0] + a  # o meio é o primeiro intervalo + a
        novo = [mid, interv[id][1]]  # e criamos um novo intervalo, iniciando desse meio, e indo até o segundo intervalo
        interv[id][1]  = mid -1  # e o intervalo anterior, tem seu segundo valor trocado para a metade - 1
    else: # caso contrario
        mid = interv[id][0] - a  # o meio é o inicial - a
        novo = [mid, interv[id][1]] # o novo parte do meio e vai até o segundo
        interv[id][1]=mid+1  # e o intervalo antigo agora vai até o meio + 1
    
    interv.append(novo)  # adicionamos o novo intervalo criado à lista de intervalos
    for i in range(len(interv) - 1, id + 1, -1): # do último até o depois de onde o intervalo alcançava a distância maxima
        interv[i], interv[i-1] = interv[i-1], interv[i]  # invertemos 


def soma (a, b):
    global interv
    sum= 0
    resp= 0

    for i in range(len(interv)):
        qtd = abs(interv[i][0] -interv[i][1]) + 1  # "distância"
        if sum + qtd>= a and sum + qtd<= b:  # se a "distância" estiver contida no intervalo
            resp += ((interv[i][0] +interv[i][1]) * qtd) // 2   # fazemos uma soma aritmética do intervalo 
        sum += qtd

    return resp

def inverte (a, b):
    global interv
    sum = 0
    ini = 0
    fim = 0

    for i in range(len(interv)):
        if sum == a-1:  # quando a "distancia" acumulada for igual ao inicio do intervalo - 1
            ini = i  # definimos o inicio do intervalo
        qtd = abs(interv[i][0]-interv[i][1]) + 1
        if sum + qtd == b:  # já se o intervalo for igual ao final do intervalo
            fim = i  # definimos o seu fim
        sum += qtd
    
    for i in range(ini, ((ini + fim) // 2) + 1):  # do inicio até metade do intervalo
        interv[i], interv[fim-(i-ini)] = interv[fim-(i-ini)], interv[i]  # invertemos os intervalos
    for i in range(ini, fim + 1):        # agora do inicio até o fim
        interv[i][0], interv[i][1] = interv[i][1], interv[i][0]  # invertemos onde começa e onde termina os intervalos

def main(entrada=input, test=False):
    global n, interv
    n, m = map(int, entrada().split())

    interv = [[1, n]]    
    r = []
    for _  in range(m):
        op, a, b = entrada().split()
        a = int(a)
        b = int(b)

        cut(a-1)  # realizamos o corte para o inicial
        cut(b)  # e para o final

        if op == "S":            
            if test:
                r.append(str(soma(a, b)))
            else:
                print(soma(a, b))
        else:            
            inverte(a, b)

    if test:
        return r

if __name__ == '__main__':
    main()