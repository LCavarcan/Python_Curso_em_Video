#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt

cat1 = float(input("Digite o valor de um cateto: "))
cat2 = float(input("Digite o valor do outro cateto: "))

hip = sqrt(cat1*cat1 + cat2*cat2) #Tem a função math.hypot que já calcula a hipotenusa

print("A hipotenusa do triangulo com catetos {} e {} vale {}".format(cat1, cat2, hip))