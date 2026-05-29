# 🤖 Automação com Python + PyAutoGUI

Um projeto simples de automação de desktop em Python, utilizando `PyAutoGUI` para simular interações de mouse e teclado em uma janela do navegador.

## ✨ Visão geral

Este projeto demonstra como automatizar tarefas repetitivas no sistema operacional, abrindo o navegador, navegando até a barra de pesquisa e realizando uma busca automática.

A automação foi desenvolvida em `Python` com foco em simplicidade, clareza e execução direta.

## 🚀 Funcionalidades

- Aguarda alguns segundos antes de iniciar a automação
- Move o cursor e clica no navegador
- Abre a barra de pesquisa
- Digita uma busca automática
- Pressiona Enter para executar a pesquisa

## 📁 Estrutura do projeto

```text
Projeto Automação com Python + PyAutoGUI/
├── Main.py
└── README.md
```

## 🧰 Requisitos

- Python 3.x
- `pyautogui`

## 🔧 Instalação

1. Clone ou abra este projeto em sua máquina.
2. Instale a dependência:

```bash
pip install pyautogui
```

## ▶️ Como executar

Execute o script principal:

```bash
python Main.py
```

> Observação: antes da execução, certifique-se de que o navegador e a posição da janela estejam adequados, pois a automação depende de coordenadas da tela.

## ⚠️ Observações importantes

- O `pyautogui.FAILSAFE = True` foi ativado para permitir interrupção segura da automação.
- A propriedade de coordenadas usadas no script pode variar entre máquinas e resoluções diferentes.

## 📝 Autor

Projeto desenvolvido com Python e PyAutoGUI para demonstração de automação desktop.
