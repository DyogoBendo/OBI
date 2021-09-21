class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return self.x < other.x 

def cross(p0, p1, p2):
    return (p1.x - p0.x) * (p2.y - p0.y) - (p2.x - p0.x) * (p1.y - p0.y)
    # retorna se o segmento p0p1 está mais próximo do segmento p0p2 em sentido horário ou anti-horário
    # se o resultado é positivo, então p0p1 está em sentido horário de p0p2, se é negativo, está em sentido anti-horário


def main(entrada=input, test=False):
    n = int(entrada())    
    pontos = [Ponto(0, 0) for _ in range(n)]
    ch = [0 for i in range(n)]  # envoltorio convexo      
    for i in range(n):        
        pontos[i].x, pontos[i].y = map(int, entrada().split())
    pontos.sort()         
    nch = 0  # número de pontos no envoltório convexo

    for i in range(n):
        while nch > 1 and cross(pontos[ch[nch-2]], pontos[ch[nch-1]], pontos[i]) >= 0:
            # enquanto tivermos ao menos dois pontos no envoltório para analisar
            # e  a comparação for de que o último ponto do envoltório não está em sentido anti horário em relação ao ponto i que estamos avaliando
            nch -= 1  # "recuamos" na análise dos pontos do envoltório
            # isso quer dizer que, o ponto que antes fazia parte do envotório, agora estará contido pelo novo ponto considerado no envoltório
        ch[nch] = i  # adicionamos o ponto i como o último ponto do envoltório até então
        nch += 1  # aumentamos a quantidade de pontos no envoltório
    print(ch)
    k = nch - 1  # o número de saltos é exatamente o número de pontos no envoltório, menos 1, pois não é realizado nenhum salto para se chegar no ponto inicial

    if not test:
        print(k)
    else:
        return [k]

if __name__ == '__main__':
    main()