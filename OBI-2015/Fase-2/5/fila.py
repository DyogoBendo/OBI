def main(file_input=input, test=False):
    n = int(file_input())
    fila = list(map(int, file_input().split()))
    q = int(file_input())
    for j in range(q):
        t, i, x = map(int, file_input().split())
        if t == 0:
            fila.insert(i, x)
        else:
            c = 0
            for k in range(i - 2, -1, -1):
                if fila[k] > fila[i - 1] + x:
                    c = k + 1
                    break
            if not test:                
                print(c)
            else:
                return [c]
            
            


if __name__ == '__main__':
    main()