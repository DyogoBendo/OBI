from math import sqrt
from sys import stdin

# n log n

def search(circulos, i, j, distancia):    
    if i > j:
        return False
    m = int((i + j) / 2)            
    if circulos[m][0] < distancia:
        is_borda = search(circulos, m + 1, j, distancia)
        if is_borda:
            return is_borda
        else:
                if i == j == len(circulos) - 1:                
                    return (0, 0)
                else:
                    return circulos[m + 1]

    elif circulos[m][0] > distancia:
        is_borda = search(circulos, i, m - 1, distancia)
        if is_borda:
            return is_borda
        else:
            return circulos[m]
    else:
        return circulos[m]
    


def main(file_input=stdin.readline, test=False):
    c, t = map(int, file_input().split())    

    circulos = []
    k = 0

    for i in range(c):
        ci = int(file_input())
        circulos.append((ci, c-i))

    for i in range(t):
        x, y = map(int, file_input().split())

        d = sqrt((x ** 2) + (y ** 2))

        p = search(circulos, 0, len(circulos) - 1, d)[1]
        k += p

    if not test:
        print(k)
    else:
        return [k]

if __name__ == '__main__':
    main()