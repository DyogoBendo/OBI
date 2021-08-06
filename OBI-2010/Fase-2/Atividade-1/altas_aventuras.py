from posixpath import split

from math import log2


def main(file_input=input, test=False):        
    n, k = map(int, file_input().split())

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
    