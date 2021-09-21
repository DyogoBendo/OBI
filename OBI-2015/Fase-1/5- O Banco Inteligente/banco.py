S = 5001
def main(entrada=input, test=False):        
    s = int(entrada())
    notas = list(map(int, entrada().split()))
    valores = [2, 5, 10, 20, 50, 100]

    dp = [1 if i == 0 else 0 for i in range(s + 1)]  # com o valor 0 temos uma opção: devolver nada

    for i in range(5, -1, -1):  # verificamos para cada nota partindo da de maior valor                
        for j in range(s, -1, -1):  # iniciando pelo valor desejado e descendo até chegar em 0                        
            k = 1
            while k <= notas[i] and j - k * valores[i] >= 0:  # verificamos para cada subtração possível do valor pela nota atual 
                dp[j] += dp[j-k*valores[i]]                
                k += 1            
    c = dp[s]
    
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()