from pathlib import Path
import os

PONTILHADO = "-"*100

def create_test(main, files, number_tests=11, prefix="", sufix="", start_position=0):    
    passed_all_tests = True         
    num_conjunto_testes_certos = 0     
    conjunto_testes_errados = set()  
    print(PONTILHADO)   
    for l in range(start_position, number_tests + start_position):        
        files_folder = Path(files,  prefix + str(l) + sufix)        
        print(f"\t\033[95mCONJUNTO DE TESTES {l}: \033[0m")
        print(PONTILHADO)
        passed_test_group = True

        num_testes_certos = 0
        num_testes = 0
        testes_errados = set()

        for i in range(1, (len(os.listdir(files_folder)) // 2) + 1):
            num_testes += 1
            input_filename = Path(files_folder, 'in' + str(i))        
            input_file = open(input_filename, 'r')

            result = main(entrada=input_file.readline, test=True)
            
            output_filename = Path(files_folder, 'out' + str(i))
            output_file = open(output_filename, 'r')
            passed_test = True            

            num_linhas_certas = 0
            num_linhas = 0                                                
            print(f"\t\tTESTE {i}: ")            
            for j in range(len(result)):                
                num_linhas += 1
                gabarito = output_file.readline().strip()            
                print(f"\t\t\tLINHA {j}: ")
                print(f"\t\t\tGABARITO LINHA {j}:\t", gabarito.strip())
                print(f"\t\t\tRESULTADO LINHA {j}:\t", result[j])
                print()
                if gabarito == str(result[j]):
                    num_linhas_certas += 1
                else:                    
                    passed_test = False                

            if not passed_test:
                result_print = '\033[91m' + "ERRO" + '\033[0m'
                testes_errados.add(str(i))
                passed_test_group = False
            else:
                num_testes_certos += 1
                result_print = '\033[92m' + "PASSOU" + '\033[0m'

            print(f"\t\tRESULTADO TESTE {i}: " + result_print)
            print(f"\t\tNÚMERO DE LINHAS CERTAS: {num_linhas_certas}/{num_linhas}")
            print(PONTILHADO)                 
        if not passed_test_group:
            passed_all_tests = False
            result_print = '\033[91m' + "ERRO NOS TESTES: "
            result_print += ", ".join(testes_errados)
            result_print += '\033[0m'

            conjunto_testes_errados.add(str(l))
        else:
            num_conjunto_testes_certos += 1
            result_print = '\033[92m' + "PASSOU" + '\033[0m'

        print(f"\tRESULTADO GRUPO DE TESTES {l}: " + result_print)
        print(f"\tNÚMERO DE TESTES CERTOS: {num_testes_certos}/{num_testes}")
        print(PONTILHADO)
    conjunto_testes_errados
    result_print = '\033[92m' + "PASSOU" + '\033[0m' if passed_all_tests else '\033[91m' + "ERRO NOS CONJUNTOS DE TESTES: " + ", ".join(conjunto_testes_errados) +'\033[0m'
    print("RESULTADO TOTAL: " + result_print)
    print(f"NÚMERO DE CONJUNTOS DE TESTES CERTOS: {num_conjunto_testes_certos}/{number_tests}")
    print(PONTILHADO)

    
    