def main(entrada=input, test=False):    
    n, m = map(int, entrada().split())
    peso = 0
    excedeu = False
    for i in range(n):
        s, e = map(int, entrada().split())
        peso += (e - s)
        excedeu = True if peso > m else excedeu        
    caracter = "S" if excedeu else "N"    

    if not test:
        print(caracter)
    else:
        return [caracter]

if __name__ == '__main__':
    main()