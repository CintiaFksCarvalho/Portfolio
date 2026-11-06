# Programação em C

Atividades práticas realizadas durante a formação de Técnico de Informática – Sistemas, Nível 4, com foco nos fundamentos da linguagem C, estruturas de dados, modularização e desenvolvimento de programas interativos.
As atividades foram realizadas em contexto de aprendizagem orientada pelo professor, através de explicações teóricas, demonstrações práticas e acompanhamento na resolução dos exercícios.

---

## 01. Gestor de Vetores

**Objetivo:** Criar um programa interativo para gerir um vetor de números reais (`float`), permitindo inserir, consultar, alterar valores e realizar cálculos estatísticos.

**Funcionalidades implementadas:**
- Inserção de valores no vetor.
- Visualização dos elementos armazenados.
- Cálculo da soma e média.
- Identificação do maior e menor valor.
- Alteração de valores através dos respetivos índices.
- Navegação através de menus interativos.

**Conceitos aplicados:**

| Conceito | Aplicação |
|---|---|
| Arrays de tamanho variável (VLA) | Definição do tamanho do vetor durante a execução. |
| Funções | Organização do programa em funções especializadas. |
| `switch/case` | Gestão das opções dos menus. |
| Vetores | Armazenamento e manipulação de números reais. |
| Ciclos | Percorrer elementos e controlar a execução dos menus. |
| Flags | Controlo do estado de inserção dos dados. |
| Ponteiros | Passagem de arrays para funções e alteração dos seus elementos. |

[Consultar código-fonte](https://github.com/CintiaFksCarvalho/Portfolio/blob/583c5b2e01c5608f75b4a383deb32f9aa0dd018f/Programa%C3%A7%C3%A3o_C/GestorVetoresDinamico.c)

---

## 02. Jogo de Adivinhação Customizável

**Objetivo:** Criar um jogo interativo de adivinhação com menu principal e configurações personalizáveis.

**Funcionalidades implementadas:**
- Geração de números aleatórios.
- Configuração do número de tentativas.
- Personalização da dificuldade através do limite máximo do número.
- Menu de ajuda e informações.
- Validação das entradas do utilizador.
- Controlo das tentativas e identificação de vitória.

**Conceitos aplicados:**

| Conceito | Aplicação |
|---|---|
| Bibliotecas | Utilização de `stdio.h`, `stdlib.h` e `time.h`. |
| Números aleatórios | Geração de valores através de `rand()` e `srand()`. |
| `switch/case` | Gestão das opções do menu principal. |
| Ciclos aninhados | Controlo do menu e das tentativas. |
| Validação de entradas | Verificação dos dados introduzidos através de `scanf()`. |
| Flags lógicas | Controlo do estado de vitória através de uma variável lógica. |
| Variáveis globais | Manutenção das configurações entre partidas. |

[Consultar código-fonte](https://github.com/Cintiafkscarvalho/Portfolio/blob/7fb1ee5eb7add1ed3b8ff8e9adfc8231bdd5dc33/Programa%C3%A7%C3%A3o_C/JogoAdivinhacaoCustomiz%C3%A1vel.c)

---

## Competências técnicas

Linguagem C | Lógica de Programação | Algoritmos | Vetores | Arrays de Tamanho Variável | Funções | Ponteiros | Estruturas Condicionais | Ciclos | Validação de Entradas | Resolução de Problemas.