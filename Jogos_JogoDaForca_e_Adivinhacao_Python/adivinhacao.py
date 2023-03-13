import random

def jogar():

    print("-" * 40)
    print(f"{'- JOGO DA ADIVINHAÇAO -' : ^40}")
    print("-" * 40)

    numero_secreto = random.randrange(1,101)

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        vidas = 20
    elif(nivel == 2):
        vidas = 10
    else:
        vidas = 5

    rodada = 0
    acertou = False
    while(not acertou):
        print("Tentativa {}, Vidas Restantes: {}".format(rodada + 1, vidas))

        chute = int(input("Digite um número entre 1 e 100: "))
        espacamento()
        print("Você digitou ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        else:
            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto
            rodada += 1

            if (acertou):
                print(f"{'- PARABÉNS -' : ^30}")
                print("Você acertou com {} tentativas!".format(rodada))
            else:
                vidas -= 1
                if vidas == 0:
                    print("Você perdeu! O número secreto era: {}".format(numero_secreto))
                    break
                else:
                    if (maior):
                        print("Você errou! O seu chute foi maior do que o número secreto.")
                    elif (menor):
                        print("Você errou! O seu chute foi menor do que o número secreto.")
            espacamento()


def espacamento():
    print("-" * 60)


if(__name__ == "__main__"):
    jogar()
