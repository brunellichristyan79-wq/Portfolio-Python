# 🎮 Jogo de Adivinhação de Número

O computador sorteia um número entre 1 e 100 e o jogador tenta descobri-lo, recebendo dicas de "muito baixo" ou "muito alto" a cada palpite.

## ✨ Funcionalidades

- Número secreto sorteado aleatoriamente a cada partida
- O jogador escolhe quantas tentativas quer ter
- Dicas depois de cada palpite
- Mensagem de vitória, ou de derrota revelando o número secreto

## ▶️ Como executar

É necessário ter o [Python](https://www.python.org/downloads/) instalado.

```bash
python jogo.py
```

## 💻 Exemplo de uso

```
Quantas tentativas você quer ter? 3
Tente adivinhar o numero (entre 1 a 100): 50
Muito alto! Tente um numero menor.
Tente adivinhar o numero (entre 1 a 100): 25
Muito baixo! Tente um numero maior.
Tente adivinhar o numero (entre 1 a 100): 37
Você perdeu! O numero secreto era: 41
```

## 📚 O que eu pratiquei

- Biblioteca `random` e a função `random.randint()`
- `while` com condição (`tentativas < limite`), em vez de `while True`
- Contador de tentativas (`tentativas += 1`)
- Conversão de texto para número inteiro com `int()`
- Diferença entre `==` (igual) e `!=` (diferente), além de `<` (menor)
- `break` para sair do loop quando o jogador acerta
- **`else` em um `while`**: só roda se o loop terminar sem passar por um `break`, o que resolve "o jogador perdeu" sem precisar de uma variável extra
- Decidir o que fica **dentro** do loop (palpite e dicas) e o que fica **fora** (sorteio do número secreto)

## 🐛 Desafios que resolvi no caminho

- Misturar duas ideias numa variável só (o limite de tentativas e o contador de tentativas usadas)
- Código fora de lugar por causa de indentação (`limite` dentro do `else`, `while` recuado sem motivo)
- Usar `!=` no lugar de `==` no `if` principal, o que fazia o jogo dar parabéns para qualquer palpite errado
- Usar `input()` para mostrar uma mensagem, o que fazia o programa parar esperando uma resposta

## 🔭 Melhorias futuras

- Tratar o erro caso o jogador digite letras (`try/except`)
- Perguntar se o jogador quer jogar de novo ao final
- Escolher o nível de dificuldade (faixa de números diferente)
- Dar uma dica extra, como "o número é par" ou "está perto"
- Versão com interface gráfica (Tkinter)
