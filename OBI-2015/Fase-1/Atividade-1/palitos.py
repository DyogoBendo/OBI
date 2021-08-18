from math import ceil

def main(file_input=input, test=False):
    n, m = map(int, file_input().split())

    c = 0
    if m >= n:
        for i in range(n):
            c += i
    else:        
        piso = n - 2 * m

        if piso > 0:
            k = m + 1 - piso
            for i in range(k + 1):            
                c += i
        else:
            inicial = 2*(m - (n // 2) + 1)
            for i in range(1, n - m):
                c += inicial
                inicial += 1                
            for i in range(n -m, m + 1):
                c += n - i - 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()