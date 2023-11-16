# -*- coding: utf-8 -*-
"""
"""
# Importação da biblioteca OS para clear do terminal.
# Bruna Barbour Fernandes - 23007950
# João Victor Francetto Xavier - 23003634

import os as oo 


# Definição das variáveis.

menu = 3 
itemsoma = 0
ppix = 0
ppc = 0
ppd = 0
i = 0
opcaov = " "
valortodas = 0
itenstodos = 0
venda = 0 



oo.system('cls')
print("_"*50)

# Start do sistema.>

print("\nBem vindo ao sistema, por favor cadastre sua senha!")

# Cadastro e login do usuario com senha definida.>

ss=(int)(input("\nPor favor cadastre sua senha: "))
          
sss=(int)(input("\nPor favor insira sua senha: "))

# Utilização de while para repetir a senha caso digitado errado.>

while ss!=sss:
    sss=(int)(input("\nSenha incorreta, por favor insira a senha novamente: "))
    
# Greet do sistema e inserção do saldo inicial caso a senha seja inserida corretamente.>

if ss==sss:
    oo.system('cls')
    print("\nBem vindo!")
    saldoi = float (input ("Digite o valor do saldo inicial: "))
    print ("\n")

# Utilização do while para o primeiro menu do sistema.>

    while (menu == 3):
        print ("Insira: ")
        print ("1- REGISTRAR VENDAS")
        print ("2- VALOR RECEBIDO")
        print ("3- FECHAR CAIXA")

# Input para escolha de opção do menu.>

        opcao = int (input ("Digite a opção do menu: ")) 
        print ("\n")

# validação de dados do menu

        if opcao < 0 and opcao >= 4:
            print ("Valor inválido, digite novamente! ")

# Início da cadeia de comandos caso usuário escolha a primeira opção.>

        if opcao == 1:

            venda = venda + 1 
            itemsoma = 0
            ppix = 0
            ppc = 0
            ppd = 0
            i = 0

# Enquanto a opção for diferente de 0, o menu de inserção de valor do produto continuará no display.>

            while (opcaov != "0"):
                    
# Utilização dos inputs, tanto para inserção do valor, quanto para sair ou adicionar mais produtos.>

                    item = float (input ("Insira o valor do produto: "))
                    
# Validação de dados.>
                    
                    if item < 0:
                        print ("Preço inválido!")
                        break
                    else:
                        opcaov = input ("Digite n para sair, ou s para adicionar mais produtos: ")
                        i= i+1
                        print ("\n")
                        print ("\n")

# Caso opção seja 's', armazenará a informação do valor do produto na variável itemsoma, e ira somar gradualmente conforme o comando seja dado.>

                    if opcaov == "s":
                        itemsoma = itemsoma + item 
                        i+1
                        continue 

# Caso opção seja 'n', quebrará o loop da inserção do valor dos produtos, voltando ao menu principal.>

                    if opcaov == "n":
                        itemsoma = itemsoma + item 
                        print ("\n")
                        break

# Display do valor total da compra e número de itens vendidos, seguidos da forma de pagamento.>
            
            print (f"Valor total da compra: {itemsoma: 4.2f}")
            print ("Número de itens vendidos: ", i)
            print ("\n\n")
            print ("Forma de pagamento: ")
            print (" ")
            print ("1- Pix")
            print ("2- Cartão débito")
            print ("3 - Dinheiro")
           
# Definição da variável formap, que armazena a informação da forma de pagamento.>
           
            formap = float (input ("Digite a forma de pagamento: "))

# Definição da função de cada forma de pagamento, dando suas respectivas instruções. Caso a forma de pagamento seja em dinheiro, calcula-se o troco.>

            if formap == 1:
                print ("\n")
                ppix = ppix + itemsoma
                oo.system('cls')
                print ("Realizar a leitura do QrCode e finalizar pagamento!")
                print ("Venda concluída! Obrigada")
                print ("\n\n")

            if formap == 2:
                print ("\n")
                ppc = ppc + itemsoma
                oo.system('cls')
                print ("Realizar os procedimentos da maquininha e finalizar pagamento!")
                print ("Venda concluída! Obrigada")
                print ("\n\n")

# Validação de valores, definição do valor do troco, de todos os itens e valor total da venda.>

            if formap == 3:
                print ("\n")
                ppd = ppd + itemsoma
                dinheiro = float (input ("Valor em dinheiro: "))
                troco = dinheiro - itemsoma 
                
                if dinheiro < 0:
                    print ("Valor inválido!")
                    break

                if troco < 0:
                    print ("Valor menor ao da compra!")
                    print ("\n\n")

                if troco > 0:
                    print ("Valor do troco: ", troco)
                    print ("\n\n")

            valortotalvenda = ppix + ppc + ppd
            
            valortodas = valortodas + valortotalvenda

            itenstodos = itenstodos + i


# Caso opção do menu seja '2', limpará o terminal e mostrará o valor total recebido, o número de vendas e o total de itens vendidos.>

        if opcao == 2:
            oo.system('cls')
            print (f"Valor total recebido: {valortodas:4.2f}")
            print ("Número de vendas: ", venda)
            print ("Total de itens vendidos: ", itenstodos)

            saldototal = saldoi + valortodas

            print (f"Saldo total registrado no caixa: {saldototal:4.2f}")
            print ("\n\n\n")

# Caso opção seja '3', ocorrerá a finalização do caixa e consequentemente do sistema.>

        if opcao == 3:
            oo.system('cls')
            print ("Caixa Finalizado!")
            break 


            
    
      
                     
                       
                    







