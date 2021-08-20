def main(file_input=input, test=False):
    n = int(file_input())
    l1, c1 = map(int, file_input().split())
    l2, c2 = map(int, file_input().split())

    is_possible = False
    metade = n / 2
    # checa corte horizontal
    if l1 <= metade and l2 > metade:
        is_possible = True
    if l1 > metade and l2 <= metade:
        is_possible = True
    
    # checa corte vertical

    if c1 <= metade and c2 > metade:
        is_possible = True
    if c1 > metade and c2 <= metade:
        is_possible = True
    c = "S" if is_possible else "N"

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()