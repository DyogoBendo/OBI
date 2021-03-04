def calcular_dimensoes(aa, at):
    delta = ((- 4 - aa) ** 2) - (16 * at)

    if delta < 0:
        resultado = "-1 -1"
        return resultado
    m = int(((4 + aa) - delta ** 0.5) / 4)
    n = int(((4 + aa) + delta ** 0.5) / 4)

    if n * m != at:
        resultado = "-1 -1"
        return resultado

    resultado = f'{m} {n}'

    return resultado


if __name__ == '__main__':
    azulejos_azuis = int(input())  # azulejos externos
    azulejos_brancos = int(input())  # azulejos internos
    azulejos_totais = azulejos_azuis + azulejos_brancos

    print(calcular_dimensoes(azulejos_azuis, azulejos_totais))
