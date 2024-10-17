idade = int(input("Digite uma idade: "))
if idade > 17:
    print("Pode entrar")
else:
        print("Não pode entrar")

        

num = int(input("Digite um número: "))
if num > 0:
    print("Número é positivo")
elif num < 0:
    print("Número é negativo")
else:
    print("É neutro")



num = int(input("Informe um número: "))
if num % 2 == 0:
    print("É par")
else:
    print("É impar")



ano = int (input("Digite um ano: "))
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print("É um ano bissexto")
else:
    print("Não é um ano bissexto")



peso = float (input("Insira o peso: "))
altura = float (input("Insira a altura: "))
imc = peso /(altura **2)
if imc < 18.5:
    print("Magreza")
elif imc >= 18.5 and  imc <= 24.9:
    print("Peso ideal")
else:
    print("Obeso")
    


numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
print(numero1 // numero2) #retorna apenas o numero inteiro da divisao
print(numero1 / numero2) #faz a divisao normalmente




num1 = int (input("Digite um número: "))
num2= int (input("Digite outro número: "))
if num1 > num2:
    print({num1})
    
elif num1 < num2:
    print({num2})
    
elif num1 == num2:
    print("São iguais")

not1 = float(input("Primeira nota: "))
not2 = float(input("Segunda nota: "))
media = (not1 + not2) /2
if media >= 7 and media = 10:
    print("Aprovado")
elif media <= 6.9 and media >= 4.1:
    print("Recuperação")
elif media <= 4:
    print("Reprovado")

idade= int(input("Informe sua idade: "))
if idade <= 17:
    print("Menor de idade")
elif idade >= 18 and idade  <= 60:
    print("Adulto")
elif idade > 60:
    print("Veio")
