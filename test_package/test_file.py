from pathlib import Path
import os
import time

PONTILHADO = "-"*100

ICONE_CORRETO_GRANDE = "![Correto](https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Tick_Mark_Dark-24.png)"
ICONE_ERRADO_GRANDE = "![Incorreto](https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Close_Icon_Dark-24.png)"

ICONE_CORRETO_MEDIO = "![Correto](https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Tick_Mark_Dark-18.png)"
ICONE_ERRADO_MEDIO = "![Incorreto](https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Close_Icon_Dark-18.png)"

ICONE_CORRETO_PEQUENO = "![Correto](https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Tick_Mark_Dark-12.png)"
ICONE_ERRADO_PEQUENO = "![Incorreto](https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Close_Icon_Dark-12.png)"

def create_test(main, files, number_tests=11, prefix="", sufix="", start_position=0):    
    txt = ""
    passed_all_tests = True         
    num_conjunto_testes_certos = 0     
    conjunto_testes_errados = set()   


    parte_posterior = ""   
    for l in range(start_position, number_tests + start_position):        
        parte_testes_individuais = ""
        files_folder = Path(files,  prefix + str(l) + sufix)                
        passed_test_group = True
        num_testes_certos = 0
        num_testes = 0
        testes_errados = set()        

        for i in range(1, (len(os.listdir(files_folder)) // 2) + 1):            
            num_testes += 1
            input_filename = Path(files_folder, 'in' + str(i))        
            input_file = open(input_filename, 'r')


            start_time = time.time()
            result = main(entrada=input_file.readline, test=True)
            end_time = time.time()

            real_time = end_time - start_time
            
            output_filename = Path(files_folder, 'out' + str(i))
            output_file = open(output_filename, 'r')
            passed_test = True            

            num_linhas_certas = 0
            num_linhas = 0                                                            
            
            parte_linhas = ""            
            for j in range(len(result)):                
                num_linhas += 1
                gabarito = output_file.readline().strip()            
                parte_linhas += f"\t\t\tLinha {j}: \n" 
                parte_linhas += f"\t\t\tGabarito :\t" + gabarito.strip() 
                parte_linhas += '\n'

                parte_linhas += f"\t\t\tResultado:\t" + str(result[j])
                parte_linhas += '\n\n'                
                if gabarito == str(result[j]):
                    num_linhas_certas += 1
                else:                    
                    passed_test = False                           
            if not passed_test:                
                result_print = ICONE_ERRADO_PEQUENO
                testes_errados.add(str(i))
                passed_test_group = False
            else:
                num_testes_certos += 1
                result_print = ICONE_CORRETO_PEQUENO

            parte_testes_individuais += f"\t- ### Teste {i} - {real_time * (10**3):.2f} milissegundos: " + result_print
            parte_testes_individuais += '\n'                                    
            parte_testes_individuais += parte_linhas            

            parte_testes_individuais += '\n'

        if not passed_test_group:
            passed_all_tests = False
            result_print = ICONE_ERRADO_MEDIO
            result_print += "-> Erro no(s) Teste(s) ["
            testes_errados = list(map(int, testes_errados))
            testes_errados.sort()
            testes_errados = list(map(str, testes_errados))
            result_print += ", ".join(testes_errados)            
            result_print += "]"

            conjunto_testes_errados.add(str(l))
        else:
            num_conjunto_testes_certos += 1
            result_print = ICONE_CORRETO_MEDIO

        parte_posterior += f"- ## Grupo de Testes {l}: {num_testes_certos}/{num_testes} " + result_print
        parte_posterior += '\n'        

        parte_posterior += parte_testes_individuais
        
        parte_posterior += '\n'        
    conjunto_testes_errados = list(map(int, conjunto_testes_errados))
    conjunto_testes_errados.sort()
    conjunto_testes_errados = list(map(str, conjunto_testes_errados))
    
    result_print = ICONE_CORRETO_GRANDE if passed_all_tests else ICONE_ERRADO_GRANDE + " -> Erro no(s) Conjunto(s) de Testes [" + ", ".join(conjunto_testes_errados) + "]"
    txt += f"# Resultado dos Testes: {num_conjunto_testes_certos}/{number_tests} " + result_print 
    txt += '\n'        
    txt += '\n'                

    txt += '\n'        

    txt += parte_posterior

    return txt    