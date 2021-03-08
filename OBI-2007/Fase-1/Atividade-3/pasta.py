if __name__ ==  "__main__":
    p, n = map(int, input().split())  # entrada dos dados 
    
    posic = [0 for i in range(p)]  # criamos um vetor, com p posições, iniciando com o valor 0
    
    for i in range(n):
        entrada = int(input())
        posic[entrada - 1] += 1  # guardamos vezes cada posição aparece
    
    menor = min(posic) 
    base_case = [ value - menor for value in posic]  # reduzimos ao caso base
    
    worked = True  # variavel que estabelece se a sequência é válida
    
    # Para sequências como uma única posição, ela é sempre válida
    for i in range(1, len(base_case)):  # verificamos a partir do segundo elemento ao último
        ant = base_case[i - 1] 
        atual = base_case[i]
        
        if ant > 1:
            # como iniciamos do segundo valor, é importante verificarmos se o primeiro valor é > 1
            # pois caso tenha qualquer valor > 1 na sequência, ela é inválida
            worked = False
            break
        if ant == 0 and atual == 1: 
            # Se temos a posição anterior valendo 0, e a atual valendo 1, quer dizer que temos uma sequência 'furada', logo ela é inválida
            worked = False
            break
        if atual > 1:
            # Verificamos se o atual é > 1, pois se deixassemos essa verificação apenas para o anterior, o último elemento não seria avaliado
            worked = False
            break

    # Caso a sequência não apresente nenhuma falha, então a sequência é válida            
    if worked: 
        print("S")
    else:
        print("N")