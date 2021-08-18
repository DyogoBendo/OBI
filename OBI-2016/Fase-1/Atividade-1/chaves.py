def main(file_input=input, test=False):
    n = int(file_input())
    abre = 0
    fecha = 0
    fecha_antes_abrir = False
    for i in range(n):
        linha = file_input()
        for c in linha:
            if c == "{":
                abre += 1                
            if c == "}":
                fecha += 1
                if fecha > abre:                    
                    fecha_antes_abrir = True
    c = "S" if abre == fecha and not fecha_antes_abrir else "N"

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()