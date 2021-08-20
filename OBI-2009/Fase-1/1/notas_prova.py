if __name__ == '__main__':
    notas = list('EDCBA')
    values=[(0, 0), (1, 35), (36, 60), (61, 85), (86, 100)]
    k = int(input())
    for i in range(5):
        a, b = values[i]
        if a <= k <= b:
            print(notas[i])