def solve(i, bits, num):  # calculamos o número de números múltiplos dos primos escolhidos
    global ans    

    if num > n:
        return 
    if i == k:
        if bits == 0:  # verifica se é 0
            return
        if bits & 1:  # se é ímpar            
            ans += n // num
        else:  # se é par            
            ans -= n // num
    else:
        solve(i + 1, bits, num)
        solve(i + 1, bits + 1, num * primos[i])

def main(entrada=input, test=False):
    global primos, n, k, ans
    n, k = map(int, entrada().split())
    primos = list(map(int, entrada().split()))
    
    ans = 0
    solve(0, 0, 1)
    c = n - ans

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()