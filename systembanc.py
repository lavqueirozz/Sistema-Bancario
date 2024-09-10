import sys
#inteface
print('Olá seja bem vindo(a) ao sistema bancario DIO')
nome = input('Nos informe seu nome completo: ')
cpf = input('Nos informe agora seu CPF: ')
print('Cadastro feito com sucesso')
#pagina inicial
opcao =-1
extrato = 3000
#Operações
while opcao <= 3:
 opcao = int(input('escolha uma das opções abaixo \n [0] sair \n [1] Sacar \n [2] verificar extrato \n [3] Depositar \n '))
 if opcao == 1:
    sacar = int(input(f'{nome} informe a quantia do saque: '))
    if sacar<=500:
     print(f'Sacando quantia \n Valor sacado: R${sacar}')
     extratoAtual = extrato - sacar
     print(f'Extrato Atual: R${extratoAtual}')
    elif sacar > extrato:
     print(f'{nome} voce não possui essa quantia, tente novamente mais tarde')
    elif sacar >500:
        print('Voce ultrapassou o saldo limite de saque que é: R$500')
 elif opcao == 2:
     print(f'Exibindo extrato de {nome}... \n Extrato: R${extrato} ')
 elif opcao == 3:
     deposito = int(input('Informe o valor de deposito: '))
     print(f'Valor depositado: R${deposito}')
     valorAtual = extrato+deposito
     print(f'Extrato atual: R${valorAtual}')
 elif opcao == 0:
     sys.exit(f'Obrigada por usar nosso sistema bancario {nome} , Até Logo ')