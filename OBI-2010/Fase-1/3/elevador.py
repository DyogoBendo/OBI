if __name__ == '__main__':
    n, m = map(int, input().split())
    peso = 0
    excedeu = False
    for i in range(n):
        s, e = map(int, input().split())
        peso += (e - s)
        excedeu = True if peso > m else excedeu        
    caracter = "S" if excedeu else "N"
    print(caracter)