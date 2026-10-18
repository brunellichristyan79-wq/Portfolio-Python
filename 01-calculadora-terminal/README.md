# 🧮 Calculadora de Terminal

Meu primeiro projeto em Python: uma calculadora que roda no terminal e permite fazer várias operações seguidas sem reiniciar o programa.

## ✨ Funcionalidades

- Soma, subtração, multiplicação e divisão
- Aceita números decimais
- Trata a divisão por zero sem quebrar o programa
- Avisa quando a operação digitada é inválida
- Permite fazer várias contas seguidas (loop)

## ▶️ Como executar

É necessário ter o [Python](https://www.python.org/downloads/) instalado.

```bash
python calculadora.py
```

## 💻 Exemplo de uso

```
coloque o primeiro numero: 10
coloque o segundo numero: 5
escolha a operacao (+, -, *, / ): /
o resultado é 2.0
Deseja fazer outra operação? (s/n): n
Obrigado por usar a calculadora!
```

## 📚 O que eu pratiquei

- Variáveis e atribuição (`=`) vs comparação (`==`)
- Entrada de dados com `input()` e conversão de tipos com `float()`
- Condicionais: `if`, `elif`, `else` (inclusive um `if` dentro de outro)
- Loops com `while`, `continue` e `break`
- Indentação como parte da sintaxe do Python
- Leitura e interpretação de mensagens de erro

## 🐛 Desafios que resolvi no caminho

- `NameError` causado por usar `==` no lugar de `=`
- `IndentationError` por indentação inconsistente
- Loop que não saía porque a condição checava `"y"` enquanto a pergunta pedia `"s"`
- Duas cadeias de `if` duplicadas que faziam a divisão por zero continuar quebrando

## 🔭 Melhorias futuras

- Tratar o erro caso o usuário digite letras em vez de números (`try/except`)
- Adicionar mais operações (potência, raiz quadrada, porcentagem)
- Guardar um histórico das contas feitas
