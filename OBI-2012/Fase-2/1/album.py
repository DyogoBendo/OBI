def main(file_input=input, test=False):
    x, y = map(int, file_input().split())
    l1, h1 = map(int, file_input().split())
    l2, h2 = map(int, file_input().split())

    caso1 = l1 + l2 <= x and max(h1, h2) <= y
    caso2 = h1 + h2 <= x and max(l1, l2) <= y
    caso3 = h1 + l2 <= x and max(l1, h2) <= y
    caso4 = l1 + h2 <= x and max(h1, l2) <= y

    caso5 = l1 + l2 <= y and max(h1, h2) <= x
    caso6 = h1 + h2 <= y and max(l1, l2) <= x
    caso7 = h1 + l2 <= y and max(l1, h2) <= x
    caso8 = l1 + h2 <= y and max(h1, l2) <= x

    if not test:
        if caso1 or caso2 or caso3 or caso4 or caso5 or caso6 or caso7 or caso8:
            print("S")
        else:
            print("N")
    else:
        if caso1 or caso2 or caso3 or caso4 or caso5 or caso6 or caso7 or caso8:
            return["S"]
        else:
            return["N"]       

if __name__ == '__main__':
    main()