def cut(a):
    global n, interv
    if a >= n or a<=0:
        return
    sum=0

    id = 0
    for i in range(len(interv)):
        qtd = abs(interv[i][0] - interv[i][1]) + 1

        if qtd + sum > a:
            id = i
            break
        sum += qtd

    a -= sum
    if not a:
        return

    if interv[id][0] <= interv[id][1]:
        mid = interv[id][0] + a
        novo = [mid, interv[id][1]]
        interv[id][1]  = mid -1
    else:
        mid = interv[id][0] - a
        novo = [mid, interv[id][1]]
        interv[id][1]=mid+1
    
    interv.append(novo)
    for i in range(len(interv) - 1, id + 1, -1):
        interv[i], interv[i-1] = interv[i-1], interv[i]


def soma (a, b):
    global interv
    sum= 0
    resp= 0

    for i in range(len(interv)):
        qtd = abs(interv[i][0] -interv[i][1]) + 1
        if sum + qtd>= a and sum + qtd<= b:
            resp += ((interv[i][0] +interv[i][1]) * qtd) // 2        
        sum += qtd

    return resp

def inverte (a, b):
    global interv
    sum = 0
    ini = 0
    fim = 0

    for i in range(len(interv)):
        if sum == a-1:
            ini = i
        qtd = abs(interv[i][0]-interv[i][1]) + 1
        if sum + qtd == b:
            fim = i
        sum += qtd
    
    for i in range(ini, ((ini + fim) // 2) + 1):
        interv[i], interv[fim-(i-ini)] = interv[fim-(i-ini)], interv[i]
    for i in range(ini, fim + 1):        
        interv[i][0], interv[i][1] = interv[i][1], interv[i][0]

def main(entrada=input, test=False):
    global n, interv
    n, m = map(int, entrada().split())

    interv = [[1, n]]    
    r = []
    for _  in range(m):
        op, a, b = entrada().split()
        a = int(a)
        b = int(b)

        cut(a-1)
        cut(b)

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