#Exercícios

# Inteiros (int)
#Escreva um programa que soma dois números inteiros inseridos pelo usuário.

#num1= int(input("Digite um numero "))
#num2= int(input("Digite um numero "))
#print("Soma é {}".format(num1+num2))

#Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#Denominador = 5
#Numerador= int(input("Digite um numero "))
#resto = Numerador%Denominador
#print("O resto da divisão de {} por {} é {}".format(Numerador,Denominador,resto))

#Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#num1= int(input("Digite um numero "))
#num2= int(input("Digite um numero "))
#print("Multiplicação é {}".format(num1*num2))


#Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#Denominador = int(input("Digite o denominador "))
#Numerador= int(input("Digite o numerador "))
#print("O valor inteiro da divisão de {} por {} é {}".format(Numerador,Denominador,Numerador//Denominador))

#Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#fator = 2
#num1= int(input("Digite um numero "))
#print(num1**fator)


#Números de Ponto Flutuante (float)
#Escreva um programa que receba dois números flutuantes e realize sua adição.
#Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada
import math
pi = math.pi
r = float(input("Digite o Raio do circulo "))
A = pi * (r**2)
print("A área é {:.2f} cm2".format(A))
#f-string 
print(f"A área é {A:.2f}")

#Strings (str)
#Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#Escreva um programa que concatene duas strings fornecidas pelo usuário.


#Booleanos (bool)
#Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
#Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.