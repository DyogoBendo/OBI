def main(file_input=input, test=False):
    k = list(map(int, file_input().split()))
    j = list(map(int, file_input().split()))

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