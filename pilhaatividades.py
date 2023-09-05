def criarPilha():
    pilha = []
    return pilha

def verificarVazio(pilha):
    return len(pilha) == 0

#empilhar
def push(pilha, item):
    pilha.append(item)

#desempilhar
def pop(pilha):
    if not verificarVazio(pilha):
        return pilha.pop()
    else:
        return "A pilha está vazia, não é possivel retirar elemento"

#topo
def peek(pilha):
    if not verificarVazio(pilha):
        return pilha[-1]
    else:
        return "A pilha está vazia"

#tamanho
def size(pilha):
    return len(pilha)

#1. Escreva uma função recursiva em Python que calcule a soma dos primeiros N números inteiros positivos.

num = int(input("Insira um numero: "))

def somaNum(num):
  if num == 1:
    return 1
  else:
    return num + somaNum(num - 1)

soma = somaNum(num)

print("A soma é: ", soma)


#2. Escreva uma função recursiva para calcular o número fatorial de um número inteiro positivo.

num1 = int(input("Insira um numero: "))

def fatorial(numero):
  if numero == 1:
    return 1
  return numero * fatorial(numero - 1)

print("O numero fatorial é: ", fatorial(num1))

#3. Escreva uma função que use uma pilha para inverter uma string.
def inverteString(string):

  print(string[::-1])


string = criarPilha()

string = str(input("Digite uma palavra:"))

inverteString(string)


#4. Escreva uma função que converte um número decimal em sua representação binária usando uma pilha.

num2 = int(input("Digite o numero para o convertelo : "))

def converteBin(num2, resto):
  if num2 == 0:
    return num2

  while (num2 > 0):
    push(resto, num2 % 2)
    print(resto)
    num2 = num2 // 2
    print(num2)

  return resto
resto = criarPilha()

converteBin(num2, resto)


print("O numero convertido é: " , resto[::-1])

