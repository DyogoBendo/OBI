import time

global all_stops
def search_best_route(matriz, stops, position, end):
    time.sleep(1)
    print(position)
    global all_stops
    all_stops = []
        
    if position == end:
        all_stops.append(stops + 1)
        return

    linha = position[0]
    coluna = position[1]
    
    top = [linha - 1, coluna] if linha > 0 else False
    bot = [linha + 1, coluna] if linha < end[0] else False
    left = [linha, coluna - 1] if coluna  > 0 else False
    right = [linha, coluna + 1] if coluna < end[1] else False
    
    current_value = matrix[position[0]][position[1]]
    
    
    top_value = define_value(top)
    bot_value = define_value(bot)
    left_value = define_value(left)
    right_value = define_value(right)
    
    calcula_movimento(current_value, right_value, stops, right, matriz, end)
    calcula_movimento(current_value, bot_value, stops, bot, matriz, end)
    calcula_movimento(current_value, left_value, stops, left, matriz, end)
    calcula_movimento(current_value, top_value, stops, top, matriz, end)


def define_value(position):
    if position:
        return matrix[position[0]][position[1]]
    else:
        return 0

def calcula_acao(value):
    if value == 9:
        return 0
    else:
        return value + 1

def calcula_movimento(current_value, destiny_value, current_stop, destiny_position, matriz, end):
    while destiny_position:
        if current_value + 1 >= destiny_value:
                current_stop += 1
                time.sleep(1)
                print(destiny_position)
                print()
                search_best_route(matriz, current_stop, destiny_position, end)
                break
        else:
            current_stop += 1
            destiny_value = calcula_acao(destiny_value)
            current_value = calcula_acao(current_value)
        

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        linha = list(map(int, input().split()))
        matrix.append(linha)
    
    
    search_best_route(matrix, 0, [0, 0], [n - 1, m - 1])
    
    
    """all_stops.sort()
    
    print(all_stops[0])"""