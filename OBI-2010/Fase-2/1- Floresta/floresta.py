def main(entrada=input, test=False):        
    n = int(entrada())    
    conta = 0
    for y in range(2, (n + 1) // 2):
        x = (n - 1 + y) / ((2 * y) - 1)
        if x < y:
            break
        if x == int(x):
            conta += 1
    
    if test:
        return [conta]
    else:
        print(conta)


if __name__ == '__main__':
    main()
    