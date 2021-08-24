from posixpath import split

from math import log2


def main(entrada=input, test=False):        
    n, k = map(int, entrada().split())

    piso_log = int(log2(n)) + 1

    if piso_log <= k:
        r = piso_log
    else:
        r = "abobora"
    
    if test:
        return [r]
    else:
        print(r)

if __name__ == '__main__':
    main()
    