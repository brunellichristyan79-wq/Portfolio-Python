# Jogo de adivinhação de número
# O computador sorteia um número de 1 a 100 e o jogador tenta acertar,
# com um limite de tentativas escolhido por ele.

import random  # biblioteca para sortear números aleatórios

# o sorteio fica FORA do loop: o número secreto não pode mudar a cada palpite
numero_secreto = random.randint(1, 100)

# limite de tentativas escolhido pelo jogador, e contador de tentativas já usadas
limite = int(input("Quantas tentativas você quer ter? "))
tentativas = 0

# repete enquanto ainda restarem tentativas
while tentativas < limite:
    chute = int(input("Tente adivinhar o numero (entre 1 a 100): "))
    tentativas += 1  # conta mais uma tentativa usada

    if chute == numero_secreto:
        print("Parabéns, Você acertou!")
        break  # acertou: sai do loop (e o else abaixo NÃO roda)
    elif chute < numero_secreto:
        print("Muito baixo! Tente um numero maior.")
    else:
        print("Muito alto! Tente um numero menor.")
else:
    # o else de um while só roda se o loop terminar SEM passar por um break,
    # ou seja, quando as tentativas acabaram e o jogador não acertou
    print(f"Você perdeu! O numero secreto era: {numero_secreto}")
