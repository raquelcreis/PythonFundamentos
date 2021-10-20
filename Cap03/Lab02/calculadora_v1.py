# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")


def soma(arg1,arg2): return arg1 + arg2
def diferenca(arg1,arg2): return arg1 - arg2
def multiplicacao(arg1,arg2): return arg1*arg2
def divisao(arg1,arg2): return float(arg1/arg2)

print("\n******************* Menu *******************")
print("\n 1 - Soma")
print("\n 2 - Diferença")
print("\n 3 - Multiplicação")
print("\n 4 - Divisão")

escolha = int(input("\nQual sua opção (1,2,3,4):"))

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if escolha == 1:
    print('\nResultado: ',soma(num1,num2))
elif escolha == 2:
    print('\nResultado: ',diferenca(num1,num2))
elif escolha == 3:
    print('\nResultado: ',multiplicacao(num1,num2))
elif escolha == 4:
    print('\nResultado: ',divisao(num1,num2))
else: print('Operação inexistente na calculadora')


