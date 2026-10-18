import tkinter as tk  # biblioteca para criar janelas gráficas


# função chamada quando qualquer botão de operação for clicado
def calcular(operacao):
    # pega o texto digitado nas caixas e converte para número decimal
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())

    # decide qual conta fazer, dependendo do botão clicado
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:
            resultado = "não é possível dividir por zero"
        else:
            resultado = num1 / num2

    # atualiza o texto do rótulo de resultado, mostrando o valor calculado
    resultado_label.config(text=f"o resultado é: {resultado}")


# cria a janela principal
janela = tk.Tk()
janela.title("calculadora")
janela.geometry("300x400")

# rótulo e caixa de texto para o primeiro número
rotulo = tk.Label(janela, text="digite um número")
rotulo.pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

# rótulo e caixa de texto para o segundo número
rotulo2 = tk.Label(janela, text="digite outro número")
rotulo2.pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

# rótulo vazio, reservado para mostrar o resultado depois
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# um botão para cada operação
botao_somar = tk.Button(janela, text="+", command=lambda: calcular("+"))
botao_somar.pack()

botao_subtrair = tk.Button(janela, text="-", command=lambda: calcular("-"))
botao_subtrair.pack()

botao_multiplicar = tk.Button(janela, text="*", command=lambda: calcular("*"))
botao_multiplicar.pack()

botao_dividir = tk.Button(janela, text="/", command=lambda: calcular("/"))
botao_dividir.pack()

# mantém a janela aberta, esperando ações do usuário
janela.mainloop()
