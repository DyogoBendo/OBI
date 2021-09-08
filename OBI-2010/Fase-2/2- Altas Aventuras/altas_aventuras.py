from math import log2, ceil


def main(entrada=input, test=False):        
    n, k = map(int, entrada().split())

    piso_log = int(log2(n)) + 1    

    if piso_log <= k:
        r = piso_log
    else:    
        r = 0
        while k > 1:
            r += 1
            n = ceil((n - 1) / 2)
            k -= 1
        r += n

    if test:
        return [r]
    else:
        print(r)

if __name__ == '__main__':
    main()
    