frase = str(input("Digite uma frase: "))

print("A letra A aparece", frase.lower().count('a'), "vezes na frase")
print("A primeira letra A apareceu na posicao", frase.strip().lower().find('a')+1)

i=0

while(frase.strip().count('a', i, len(frase))>1):
    i=i+1


print("A ultima letra A apareceu na posicao", frase.strip().lower().find('a', i, len(frase))+1)