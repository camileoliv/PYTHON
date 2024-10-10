#Saida de dados

"""nome= "Joshua"
idade= 19
peso= 75

#forma antiga
print("O meu nome é %s" %nome)
print("%s tem %d de idade %.1f peso"%(nome, idade, peso))

#forma mais nova
print ("{} tem {} anos {} peso.".format(nome, idade, peso))

#forma novissima
print(f"{nome} tem {idade} peso {peso}")"""


#Entrada de dados

hw= input("Escreva 'Alô mundo': ")
print({hw})


num= int (input("Escreva um número: "))
print({num})

num1= int (input("Escreva um número: "))
num2= int (input("Escreva mais um número: "))
print({num1+num2})


n1= int (input("Primeira nota: "))
n2= int (input("Segunda nota: "))
n3= int (input("Terceira nota: "))
n4= int (input("Quarta nota: "))
print({(n1+n2+n3+n4)/4})

mc= int (input("Digite a metragem que irá ser convertida: "))
print({mc * 100})
