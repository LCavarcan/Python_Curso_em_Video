#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome = str(input('Digite um nome completo: '))

divido = nome.split()

print("""\nNome com todas as letras maiusculas: {}
Nome com todas as letras minusculas: {}
O nome tem ao todo {} letras
O primeiro nome tem {} letras""".format(nome.upper(), nome.lower(), len(nome.replace(' ', '')), len(divido[0])))