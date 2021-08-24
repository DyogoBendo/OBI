def main(entrada=input, test=False):
    n = int(entrada())
    l1, c1 = map(int, entrada().split())
    l2, c2 = map(int, entrada().split())

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