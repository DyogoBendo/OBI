from pathlib import Path
import os

PONTILHADO = "-"*100

ICONE_CORRETO = "![Correto](https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Tick_Mark_Dark-24.png)"
ICONE_ERRADO = "![Incorreto](https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Close_Icon_Dark-24.png)"

def create_test(main, files, number_tests=11, prefix="", sufix="", start_position=0):    
    txt = ""
    passed_all_tests = True         
    num_conjunto_testes_certos = 0     
    conjunto_testes_errados = set()   

    parte_posterior = ""   
    for l in range(start_position, number_tests + start_position):        
        files_folder = Path(files,  prefix + str(l) + sufix)        
        parte_posterior += f"## CONJUNTO DE TESTES {l}: \n" 
        parte_posterior += PONTILHADO + '\n'        
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
            parte_posterior += f"### \t\tTESTE {i}: \n" 
            for j in range(len(result)):                
                num_linhas += 1
                gabarito = output_file.readline().strip()            
                parte_posterior += f"####\t\t\tLINHA {j}: \n" 
                parte_posterior += f"\t\t\tGABARITO LINHA {j}:\t" + gabarito.strip() 
                parte_posterior += '\n'

                parte_posterior += f"\t\t\tRESULTADO LINHA {j}:\t" + str(result[j])
                parte_posterior += '\n'                
                if gabarito == str(result[j]):
                    num_linhas_certas += 1
                else:                    
                    passed_test = False                

            if not passed_test:                
                result_print = ICONE_ERRADO
                testes_errados.add(str(i))
                passed_test_group = False
            else:
                num_testes_certos += 1
                result_print = ICONE_CORRETO

            parte_posterior += f"### \t\tRESULTADO TESTE {i}: " + result_print
            parte_posterior += '\n'
            
            parte_posterior += f"### \t\tNÚMERO DE LINHAS CERTAS: {num_linhas_certas}/{num_linhas}" 
            parte_posterior += '\n'

            parte_posterior += PONTILHADO
            parte_posterior += '\n'

        if not passed_test_group:
            passed_all_tests = False
            result_print = "ERRO NOS TESTES: "
            result_print += ", ".join(testes_errados)            

            conjunto_testes_errados.add(str(l))
        else:
            num_conjunto_testes_certos += 1
            result_print = ICONE_CORRETO

        parte_posterior += f"\t## RESULTADO GRUPO DE TESTES {l}: " + result_print
        parte_posterior += '\n'

        parte_posterior += f"\t## NÚMERO DE TESTES CERTOS: {num_testes_certos}/{num_testes}"                 
        parte_posterior += '\n'

        parte_posterior += PONTILHADO        
        parte_posterior += '\n'        
    conjunto_testes_errados
    result_print = ICONE_CORRETO if passed_all_tests else "ERRO NOS CONJUNTOS DE TESTES: " + ", ".join(conjunto_testes_errados)

    txt += "# Resultado dos testes: " + result_print 
    txt += '\n'        
    txt += '\n'        
    
    txt += f"# NÚMERO DE CONJUNTOS DE TESTES CERTOS: {num_conjunto_testes_certos}/{number_tests}" 
    txt += '\n'             
    
    txt += PONTILHADO 
    txt += '\n'        

    txt += parte_posterior

    return txt    