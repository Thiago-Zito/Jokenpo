jg1 = input("Jogador 1, digite Pedra, Papel ou Tesoura: ")
jg2 = input("Jogador 2, digite Pedra, Papel ou Tesoura: ")

if (jg1 == "pedra" and jg2 == "tesoura" or  jg1 == "tesoura" and jg2 == "papel" or jg1 == "papel" and jg2 == "pedra"):
    print("Jogadro 1 venceu!")
elif jg1 == jg2:
    print("Empate!")
else:
    print("Jogador 2 ganhou!")
if (jg2 == "pedra" and jg1 == "tesoura" or  jg2 == "tesoura" and jg1 == "papel" or jg2 == "papel" and jg1 == "pedra"):
    print("Jogadro 2 venceu!")
else:
    print("Inválido")