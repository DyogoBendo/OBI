def main(entrada=input, test=False):
    n = int(entrada())
    abre = 0
    fecha = 0
    fecha_antes_abrir = False
    for i in range(n):
        linha = entrada()
        for c in linha:  # verificamos cada caracter em cada linha
            if c == "{":  # se está abrindo chaves
                abre += 1                
            if c == "}":  # se está fechando
                fecha += 1
                if fecha > abre:  # se estiver fechando mais elementos do que tem aberto        
                    fecha_antes_abrir = True  # significa que estamos fechando algo que ainda não foi aberto!
    c = "S" if abre == fecha and not fecha_antes_abrir else "N"  # se nunca fecharmos antes de abrir e fecharmos tudo que abrimos então é válido

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()