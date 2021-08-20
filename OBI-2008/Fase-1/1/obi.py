if __name__ == '__main__':
    n, p = map(int, input().split())
    c = 0
    for i in range(n):
        f1, f2 = map(int, input().split())
        if f1 + f2 >= p:
            c += 1
    print(c)            

    