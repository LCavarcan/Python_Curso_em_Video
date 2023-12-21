#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, pi

angulo = float(input("Digite o valor de um angulo em graus: "))

angulo = pi * angulo/180 #math.radians já transforma o angulo de graus em radianos

print("O seno desse angulo vale {:.2f} \nO cosseno desse angulo vale {:.2f}\nA tangente desse angulo vale {:.2f}".format(sin(angulo), cos(angulo), tan(angulo)))