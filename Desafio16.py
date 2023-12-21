#Crie um programa que leia um numero real qualquer pelo teclado, e mostre na tela a sua porção inteira

from math import trunc

num = float(input("Digite um numero real: "))

print("A porção inteira do numero {} é {}".format(num, trunc(num))) #int(num) -> mesma coisa que trunc(num)