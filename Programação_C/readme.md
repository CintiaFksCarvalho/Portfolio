# Programação em C

<h2>Exercício Gestor de Vetores Dinâmico</h2>

**[Ver código completo](https://github.com/CintiaFksCarvalho/Portfolio/blob/main/Programa%C3%A7%C3%A3o_C/Gestor%20de%20Vetores%20Din%C3%A2mico.c)**

## O que foi pedido
Criar um programa interativo para gerir um **vetor dinâmico de números reais (float)** com as seguintes funcionalidades:
- Inserção de valores
- Visualização dos dados  
- Cálculos estatísticos (soma, média, máximo, mínimo)
- Alteração de valores específicos
- Interface com menus

## 🛠️ Conceitos utilizados

| Conceito | Uso no programa |
|----------|----------------|
| **VLAs** | `float vetor[tam]` - tamanho definido em runtime |
| **Funções** | 10 funções modulares (I/O, cálculos, menus) |
| **Switch/Case** | Menus principal e submenu com validação |
| **Arrays/Vetores** | Manipulação completa com índices dinâmicos |
| **Loops** | `for` (percorrer vetor), `do-while` (menus), `while` (validação índice) |
| **Flags** | `inserido` para controlar estado do vetor |
| **Ponteiros** | Parâmetros `float *v` para modificação de arrays |


<h2>Exercício Jogo de Adivinhação Customizável<h2/>

**[Ver código completo](https://github.com/CintiaFksCarvalho/Portfolio/blob/main/Programa%C3%A7%C3%A3o_C/Jogo%20de%20Adivinha%C3%A7%C3%A3o%20Customiz%C3%A1vel.c)**

## O que foi pedido
Criar um **jogo de adivinhação interativo** com menu principal e configurações personalizáveis:
- Jogo principal com número aleatório
- Configurar número de tentativas
- Configurar dificuldade (limite máximo do número)
- Ajuda/informações
- Tratamento robusto de erros

## 🛠️ Conceitos utilizados

| Conceito | Uso no programa |
|----------|----------------|
| **Bibliotecas** | `stdio.h`, `stdlib.h`, `time.h` (rand/srand) |
| **Números aleatórios** | `srand(time(NULL))`, `rand() % limite` |
| **Switch/Case complexo** | Menu com 5 opções + validação |
| **Loops aninhados** | `do-while` (menu), `while` (tentativas) |
| **Validação entrada** | `scanf()` com limpeza buffer `getchar()` |
| **Flags lógicas** | `acertou` para controle de vitória |
| **Variáveis globais** | Configurações persistentes entre jogos |

