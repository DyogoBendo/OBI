def main(entrada=input, test=False):
    k = list(map(int, entrada().split()))
    j = list(map(int, entrada().split()))

    k.sort()
    a, b = k[0], k[1]

    j.sort()
    l, h = j[0], j[1]    
        

    if not test:
        if a <= l and b <= h:
            print("S")
        else:
            print("N")
    else:
        if a <= l and b <= h:
            return["S"]
        else:
            return["N"]

if __name__ == '__main__':
    main()