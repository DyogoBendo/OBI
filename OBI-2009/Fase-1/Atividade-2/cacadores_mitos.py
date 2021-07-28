if __name__ == '__main__':
    n = int(input())
    quadrantes_registrados = set()
    quadrantes_totais = []
    for i in range(n):
        coordenadas = tuple(map(int, input().split()))
        quadrantes_registrados.add(coordenadas)
        quadrantes_totais.append(coordenadas)
    
    if len(quadrantes_totais) == len(quadrantes_registrados):
        print(0)
    else:
        print(1)
