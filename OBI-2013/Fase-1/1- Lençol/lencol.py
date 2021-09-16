def main(entrada=input, test=False):
    a1, a2, b1, b2, a, b = map(int, entrada().split())

    # o que fazemos é unir uma parte com a outra, as duas restantes, pegamos a menor, pois o que sobra dessa dimensão será cortado fora
    caso1 = a1 + b1 >= a and min(a2, b2) >= b  
    caso2 = a2 + b2 >= a and min(a1, b1) >= b
    caso3 = a1 + b1 >= b and min(a2, b2) >= a
    caso4 = a2 + b2 >= b and min(a1, b1) >= a

    # apenas invertemos
    caso5 = a1 + b2 >= a and min(a2, b1) >= b
    caso6 = a2 + b1 >= a and min(a1, b2) >= b
    caso7 = a1 + b2 >= b and min(a2, b1) >= a
    caso8 = a2 + b1 >= b and min(a1, b2) >= a

    # casos em que os panos existentes já são suficientes
    caso9 = a1 >= a and a2 >= b
    caso10 = b1 >= a and b2 >= b
    caso11 = a1 >= b and a2 >= a
    caso12 = b1 >= b and b2 >= a


    if not test:
        if caso1 or caso2 or caso3 or caso4 or caso5 or caso6 or caso7 or caso8 or caso9 or caso10 or caso11 or caso12:
            print("S")
        else:
            print("N")
    else:
        if caso1 or caso2 or caso3 or caso4 or caso5 or caso6 or caso7 or caso8 or caso9 or caso10 or caso11 or caso12:
            return["S"]
        else:
            return["N"]

if __name__ == '__main__':
    main()