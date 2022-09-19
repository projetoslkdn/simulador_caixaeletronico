# IMEUSP - BMAC0110 - Introdução à Computação - Prof. Dr. Marcílio
# Aluna: Ana Clara Silva de Moraes - R.A: 7161611 - EP1 -Dispensador de Notas

# Looping infinito permite várias entradas
while True:
        
# Pedir e ler a entrada
        print (' ************** Dispensador de Notas ************** ')
        v= int (input ('\n''Digite o valor que deseja sacar. Nota mínima disponível - R$10,00: '))
        
#verifica se a entrada do usuário atende as condições de ser um numero positivo maior ou igual a 10 e divisível por 10
        if v%10==0 and v>=10: 
                print ('\n''Primeira opção: Valor do saque: R$', v,',00') # notas disponíveis: 100, 50, 20 e 10
                print ('Nota Quantidade')
                if v//100!=0:
                        if v%100//50!=0:
                                if v%100%50//20!=0:
                                        if v%100%50%20//10!=0: #com notas de 100 reais, 50 reais, 20 reais e 10 reais
                                                print ('100 ', v//100)
                                                print (' 50 ', v%100//50)
                                                print (' 20 ', v%100%50//20)
                                                print (' 10 ', v%100%50%20//10)
                                        else:                  #com notas de 100, 50, 20
                                                print ('100 ', v//100)
                                                print (' 50 ', v%100//50)
                                                print (' 20 ', v%100%50//20)
                                else:
                                        if v%100%50%20//10!=0: #com notas de 100, 50 e 10
                                                print ('100 ', v//100)
                                                print (' 50 ', v%100//50)
                                                print (' 10 ', v%100%50//10)
                                        else:                   #com notas de 100, 50
                                                print ('100 ', v//100)
                                                print (' 50 ', v%100//50)
                        else:
                                if v%100%50//20!=0:
                                        if v%100%50%20//10!=0: #com notas de 100, 20 e 10
                                                print ('100 ', v//100)
                                                print (' 20 ', v%100//20)
                                                print (' 10 ', v%100%20//10)
                                        else:                  # com notas de 100, 20
                                                print ('100 ', v//100)
                                                print (' 20 ', v%100//20)
                                else:
                                        if v%100%50%20//10!=0: #com notas de 100, 10
                                                print ('100 ', v//100)
                                                print (' 10 ', v%100//10)
                                        else:                  #com notas de 100
                                                print ('100 ', v//100)
                else:
                        if v%100//50!=0:
                                if v%100%50//20!=0:
                                        if v%100%50%20//10!=0: #com notas de 50, 20 e 10
                                                print (' 50 ', v//50)
                                                print (' 20 ', v%50//20)
                                                print (' 10 ', v%50%20//10)
                                        else:                   #com notas de 50, 20
                                                print (' 50 ', v//50)
                                                print (' 20 ', v%50//20)
                                else:
                                        if v%100%50%20//10!=0: #com notas de 50 e 10
                                                print (' 50 ', v//50)
                                                print (' 10 ', v%50//10)
                                        else:                   #com notas de 50
                                                print (' 50 ', v//50)
                        else:
                                if v%100%50//20!=0:
                                        if v%100%50%20//10!=0: #com notas de 20 e 10
                                                print (' 20 ', v//20)
                                                print (' 10 ', v%20//10)
                                        else:                   # com notas de 20
                                                print (' 20 ', v//20)
                                else:
                                        if v%100%50%20//10!=0: #com notas de 10
                                                print (' 10 ', v//10)
                                                
                print ('\n''Segunda opção: Valor do saque: R$', v,',00') # acabaram as notas de 100 reais
                print ('Nota Quantidade')
                #verificar, caso a caso, se as divivões por 20 e por 10, bem como o resto das diviões são iguais ou diferentes de zero
                if v//50!=0:
                        if v%50//20!=0:
                                if v%50%20//10!=0: # com notas de 50, 20 e 10
                                        print (' 50 ', v//50)
                                        print (' 20 ', v%50//20)                
                                        print (' 10 ', v%50%20//10)
                                else:              #com notas de 50, 20
                                       print (' 50 ', v//50)
                                       print (' 20 ', v%50//20)
                        else:
                                if v%50%20//10!=0: # com notas de 50, 10
                                        print (' 50 ', v//50)              
                                        print (' 10 ', v%50//10)
                                else:              #com notas de 50
                                       print (' 50 ', v//50)
                else:
                        if v%50//20!=0:
                                if v%50%20//10!=0: # com notas de 20 e 10
                                        print (' 20 ', v//20)                
                                        print (' 10 ', v%20//10)
                                else:              #com notas de 20
                                       print (' 20 ', v//20)
                        else:
                                if v%50%20//10!=0: #com notas 10              
                                        print (' 10 ', v//10)

                print ('\n''Terceira opção: Valor do saque: R$', v,',00')# acabaram as notas de 100 reais e de 50 reais
                print ('Nota Quantidade')
                #verificar, caso a caso, se as divivões por 20 e por 10, bem como o resto das diviões são iguais ou diferentes de zero
                if v//20!=0 and v%20//10!=0:       #com notas de 20 e 10
                        print (' 20 ', v//20)
                        print (' 10 ', v%20//10)
                else:                              #somente com notas 10
                        print (' 10 ', v//10)
                
                print ('\n''Quarta opção:  Valor do saque: R$', v,',00') # acabaram as notas de 100 reais, de 50 reais e de 20 reais
                if v//10!=0:                       #com notas 10
                        print ('Nota Quantidade')
                        print (' 10 ', v//10)
                        
        #Solicita outro valor de entrada caso a entrada não seja positiva e divisível por 10 
        if v%10!=0 and v>0:                        
                print ('Erro! Digitar um valor multiplo de R$10,00')
        #finaliza o loop quando a entrada é negativa ou zero
        if v<=0: 
                print (' ************** Sessão finalizada! ************** ')
                break
