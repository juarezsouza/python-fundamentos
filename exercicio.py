# Criação das Variáveis
nome = 'Juarez'
idade = 31

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# para imprimir alguma palavra 
print('j','u','a','r','e','z',sep='\n')

# arredondar um número em Python e exibi-lo com um número específico de casas decimais
pi = 3.14159
print(f'Valor arredondado de pi é: {pi:.2f}')

# As aspas triplas (''' ou """) são usadas para criar strings que abrangem várias linhas. 
# Elas são úteis quando você precisa incluir quebras de linha e manter o formato do texto.
# print() e sua sintaxe e recursos, que oferecem diversas maneiras de formatar e exibir mensagens;
print('''Camiseta Unissex
Tamanho: P, M, G, GG
Material: 100% algodão
Cores disponíveis: Preto, Branco, Vermelho''')

#criar um simples script em Python que coleta o nome de um departamento e o nome da pessoa responsável por ele, 
# para depois imprimir uma mensagem personalizada.
# input() para receber uma informação do usuário e como armazenar ela para utilizarmos no nosso código;
departamento = input("Digite o nome do departamento: ")
responsavel = input("Digite o nome da pessoa responsável: ")
print("O departamento de " + departamento + " é liderado por " + responsavel + ".")

# A palavra 'def' define a função
def saudar(nome):
  print(f'Olá, {nome}!')
# Agora, podemos chamar a função para executá-la
saudar('João')
saudar('Maria')

#1 - Solicite ao usuário que insira um número e,
# em seguida, use uma estrutura if else para determinar 
# se o número é par ou ímpar.
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')

#2 - Pergunte ao usuário sua idade e, com base nisso, 
# use uma estrutura if elif else para classificar a idade 
# em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.
# if condicao: Este bloco de código é executacodo se a ndicao for True
#else se for false
#elif é uma abreviação de "else if" (senão se).
# Ela é usada em conjunto com o if para testar múltiplas 
# condições em sequência quando a primeira condição do if é falsa.
idade = int(input('Digite sua idade: '))
if 0 < idade <= 12:
    print('Criança')
elif 13 <= idade <= 18:
    print('Adolescente')
elif idade > 18:
    print('Adulto')
else:
    print('Idade inválida')

#3 - Solicite um nome de usuário e uma senha e use uma 
# estrutura if else para verificar se o nome de usuário e a 
# senha fornecidos correspondem aos valores esperados 
# determinados por você.
usuario_correto = 'juarez'
senha_correta = 123456

nome = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')
#A linha if nome == 'juarez' and senha == 123456: pode ser 
# traduzida como: "Se a variável nome for igual a 'juarez' 
# E a variável senha for igual a 123456, então execute o 
# código a seguir" sendo assim correta.
if nome == 'juarez' and senha == 123456: 
    print('Acesso concedido')
else :
    print('Acesso negado')

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma 
# estrutura if elif else para determinar em qual quadrante do plano cartesiano o 
# ponto se encontra de acordo com as seguintes condições:
#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")