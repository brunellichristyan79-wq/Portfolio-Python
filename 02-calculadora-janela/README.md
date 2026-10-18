# 🖥️ Calculadora com Interface Gráfica

Evolução da calculadora de terminal: agora com uma janela de verdade, caixas de texto e um botão para cada operação.

<!-- Dica: tire um print da janela, salve nesta pasta como "screenshot.png"
     e troque esta linha por:  ![Calculadora](screenshot.png)  -->

## ✨ Funcionalidades

- Janela com dois campos para digitar os números
- Quatro botões: `+`, `-`, `*` e `/`
- Resultado exibido na própria janela
- Mensagem amigável ao tentar dividir por zero

## ▶️ Como executar

É necessário ter o [Python](https://www.python.org/downloads/) instalado. O Tkinter já vem junto com ele, então **não é preciso instalar nada extra**.

```bash
python calculadora_gui.py
```

## 📚 O que eu pratiquei

- Biblioteca **Tkinter**: `Tk`, `Label`, `Entry`, `Button`
- Posicionamento de elementos com `.pack()`
- Ler o que o usuário digitou com `.get()` e atualizar a tela com `.config()`
- Loop de eventos (`mainloop`): o programa espera cliques em vez de rodar de cima a baixo
- **Funções com parâmetro** (`def calcular(operacao)`), reaproveitadas pelos 4 botões
- `lambda` para passar um argumento diferente para cada botão
- **f-strings** para montar o texto do resultado

## 🐛 Desafios que resolvi no caminho

- Esquecer o `.` em `janela.title(...)`, o que gerava um `NameError`
- Botão chamando uma função com nome diferente da que foi definida
- Botões criados **dentro** da função, então nunca chegavam a aparecer
- Código escrito depois do `mainloop()`, que nunca era executado
- Duas funções com o mesmo nome, em que o Python usava só a última

## 🔭 Melhorias futuras

- Tratar o erro caso o usuário digite texto no lugar de número
- Melhorar o visual (cores, fontes, tamanho dos botões, layout em grade)
- Transformar em uma calculadora com teclado numérico, como as de celular
