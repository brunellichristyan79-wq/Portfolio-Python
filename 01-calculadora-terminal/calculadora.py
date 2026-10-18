# Calculadora de terminal
# Faz soma, subtração, multiplicação e divisão, e permite várias contas seguidas.

while True:  # loop infinito: só termina quando o usuário escolhe sair (break)
    # pede os dois números e converte o texto digitado para número decimal
    num1 = float(input("coloque o primeiro numero: "))
    num2 = float(input("coloque o segundo numero: "))
    operacao = input("escolha a operacao (+, -, *, / ): ")

    # decide qual conta fazer de acordo com a operação escolhida
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        # evita o erro ZeroDivisionError checando o divisor antes
        if num2 == 0:
            resultado = "esse numero não pode ser dividido por 0"
        else:
            resultado = num1 / num2
    else:
        resultado = "operação inválida"

    print("o resultado é", resultado)

    # pergunta se o usuário quer continuar
    continuar = input("Deseja fazer outra operação? (s/n): ")
    if continuar == "s":
        continue  # volta para o início do loop
    elif continuar == "n":
        print("Obrigado por usar a calculadora!")
        break  # sai do loop e encerra o programa
