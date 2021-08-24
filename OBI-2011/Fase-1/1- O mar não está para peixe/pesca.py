def main(entrada=input, test=False):
    n = int(entrada())    
    mar = [[False for _ in range(101)] for _ in range(101)]
    for _ in range(n):
        xi, xf, yi, yf = map(int, entrada().split())

        for i in range(xi, xf):
            for j in range(yi, yf):                
                mar[i][j] = True
        
        c = 0
        for i in range(101):
            for j in range(101):
                if mar[i][j]:
                    c += 1
  

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()