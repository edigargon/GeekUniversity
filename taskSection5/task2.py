"""
    2. Make a program that use the "while" command to display a countdown on the screen, starting at 10 and
    ending at 0. Show too a message "END!" after counting.

    PT-BR

    2. Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando em
    10 e terminando em 0. Mostre tambem uma mensagem "FIM!" após a contagem.

"""

count = 10

while count >= 0:
    print(count)
    count = count - 1

print("END!")