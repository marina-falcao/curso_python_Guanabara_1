num = int(input("Digite um número inteiro: "))

print('''Escolha uma das opções para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal ''')

opcao = int(input("Sua opção: "))
if opcao == 1:
    print("O número escolhido corresponde a:", bin(num)[2:])
elif opcao == 2:
    print("O número escolhido corresponde a:", oct(num)[2:])
elif opcao == 3:
    print("O número escolhido corresponde a:", hex(num)[2:])
else:
    print("Opção inválida, tente novamente.")

