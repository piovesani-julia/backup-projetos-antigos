print("vamos jogar!")
print("=" * 40)

import random

numero = input("tente adivinhar o numero: " )
numero = int(numero)

num = random.sample(range(1,30), 1)

if numero == num: 
    print("parabéns vc acertou")
elif  num(1,1) < numero :
    print("numero inválido")
else : print("o numero é: ", num, "mais sorte na próxima :/")

print ("=" * 40)
