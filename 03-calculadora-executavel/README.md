# 📦 Calculadora em Executável (.exe)

Este projeto documenta como transformei minhas calculadoras em Python em um arquivo **`.exe`** que abre com duplo clique, sem precisar ter o Python instalado.

O código-fonte usado está nas outras pastas:
- [`01-calculadora-terminal`](../01-calculadora-terminal)
- [`02-calculadora-janela`](../02-calculadora-janela)

## 🔧 Ferramenta utilizada

[**PyInstaller**](https://pyinstaller.org): empacota o interpretador Python, o código e as bibliotecas usadas em um único arquivo.

## ▶️ Como gerar o executável

1. Instale o PyInstaller:

```bash
pip install pyinstaller
```

2. Na pasta do projeto, gere o executável.

**Para a calculadora de terminal** (mantém a janela preta, pois usa `input()` e `print()`):

```bash
python -m PyInstaller --onefile --console calculadora.py
```

**Para a calculadora com janela** (esconde o terminal, pois já tem interface própria):

```bash
python -m PyInstaller --onefile --windowed calculadora_gui.py
```

3. O arquivo final fica na pasta `dist/`.

## 💡 O que cada opção faz

| Opção | Função |
|-------|--------|
| `--onefile` | Gera um único arquivo `.exe` em vez de vários arquivos soltos |
| `--console` | Mantém a janela do terminal (para programas que usam `input()`/`print()`) |
| `--windowed` | Esconde o terminal (para programas com interface gráfica) |

> Usei `python -m PyInstaller` em vez de `pyinstaller` direto porque o Windows não encontrava o comando no PATH. Chamando pelo Python, funciona sempre.

## 📚 O que eu aprendi

- Um `.exe` de Python não é "tradução" do código: é um **pacote** com o Python embutido, por isso o arquivo fica bem maior que o `.py`
- O executável só roda no sistema operacional em que foi gerado (um `.exe` do Windows não roda em Mac ou Linux)
- Nomes de arquivo com espaço atrapalham comandos no terminal; é melhor usar `_`
- O Windows pode exibir um aviso do SmartScreen na primeira execução, porque o arquivo é novo e sem "reputação"

## 📥 Sobre o arquivo `.exe`

Não envio o `.exe` junto com o código no repositório (arquivos gerados não devem ser versionados, por isso as pastas `build/` e `dist/` estão no `.gitignore`). Para disponibilizá-lo, o ideal é usar a aba **Releases** do GitHub.
