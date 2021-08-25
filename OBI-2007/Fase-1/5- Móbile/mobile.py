# Criamos uma classe para representar as peças
class Peca():
    def __init__(self, id) -> None:
        self.id = id
        self.filhos = []
        self.valor = 0

# Utilizamos uma função recursiva para mapear cada um dos "nós"
def calcula_peca(heap, peca):    
    # caso a peça não apresenta filhos, ou seja, seja uma folha, retorna 1
    # isso porque esse é o valor que ela representa (1 peça)
    # por mais que consideramos seu valor como 2, mas só fazemos isso porque contamos ela e sua mãe
    # só que como vamos repassar esse valor para a sua mãe, contamos apenas como 1, para não ocorrer contagem repetida
    if not peca.filhos:  
        peca.valor = 2
        return 1
    
    # Prosseguimos se a peça possui filhos
    
    fila = set()  # definimos um set, aceitando assim apenas um valor
    
    for filho in peca.filhos:
        # realizamos uma chamada recursiva para cada filho da peça atual
        val = calcula_peca(heap, heap[filho])
        
        # Agora, adicionamos o valor que aquele filho representa no set
        fila.add(val)
    
    # Como o set aceita apenas valores únicos
    # Caso tenha filhos com número de peças diferentes, temos um desequilibrio
    # Como retornamos 0 nesses casos, precisamos garantir que mesmo que todos os filhos 
    # Já estivessem em desequilíbrio, não consideramos esse caso como correto 
    if len(fila) > 1 or val == 0:
        return 0
    
    # Caso seja um único valor, e ele é diferente de 0
    else:
        # Pegamos o último valor (pois todos são iguais) e multiplicamos pela quantidade de vezes que esse valor aparece
        # Somamos 2 pois o valor que calculamos foi de número de peças dos filhos
        # Precisamos considerar ainda a própria peça e sua peça mãe
        peca.valor = val * len(peca.filhos) + 2
        
        # Retornamos o valor -1 pois é esse o valor que ele representa para sua mãe
        # Pois, a peça mãe não pode estar incluída na contagem
        # Se fizessemos isso, uma mãe com multiplas peças, seria contada inúmeras vezes
        return peca.valor - 1


def main(entrada=input, test=False):
    

    n = int(entrada())
    
    # Pensamos na estrutura como um heap, ele armazena cada uma das peças
    heap = []
    
    # Esse dicionário visa armazenar cada quais são os filhos de cada mãe 
    maes_filhos = {}

    for i in range(n):
        id, id_mae = entrada().split()
        
        # Criamos uma peça
        peca = Peca(id)
        try:
            # Tentamos inserir a posição que essa peça ocupa no heap
            # No dicionário, que possua a mãe que foi informada no input como chave
            maes_filhos[id_mae].append(i)
        except:
            # Se a chave ainda não existir, criamos ela, e adicionamos o valor dentro de um vetor
            maes_filhos[id_mae] = [i]

        # Adicionamos a peça ao heap
        heap.append(peca) 
        
    for p in heap:
        # Tentamos, para cada peça, informar quais são seus filhos, caso possuam
        try: 
            p.filhos = maes_filhos[p.id]
        except:
            pass
    
    # variavel facilitadora, para melhorar a legibilidade
    # começaremos a nossa chamada recursiva pela raiz 
    # a raiz foi informada como a peça que possui como mãe o valor 0
    # pegamos então a lista de valores que possui 0 como raiz
    # Por ser apenas um valor, podemos pegar certamento o termo da posição 0
    raiz = maes_filhos["0"][0]
    
    # Se a chamada recursiva retorna 0, quer dizer que foi mal sucedida
    # Pois, como em nenhum caso a peça raiz irá totalizar 0 peças
    # Esse número foi pensado para representar o caso mal sucedido, foi uma escolha arbitrária
    c = "mal" if calcula_peca(heap, heap[raiz]) == 0 else "bem"        
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()

# não passa em único caso de teste -> esse caso de teste não está de acordo com o próprio enunciado, que diz que existe apenas uma raiz pra cada móbile, mas o teste 5 do conjunto de testes 8 possuí 15 raízes