## 📊 **Cálculo de Média com Vetores**
[![Ver Código](https://img.shields.io/badge/Ver_Código-Blue?style=for-the-badge&logo=github)](link-do-teu-codigo-java)

**O que foi pedido:** Criar programa que lê 3 idades num **array**, mostra os valores inseridos e calcula a média aritmética.

### 🛠️ **Conceitos principais**
| Arrays | Ciclo `for` | Scanner | `.length` | Acumulador | Índices |

**Demo:** `Idade 1: 25 → Idade 2: 30 → Idade 3: 35 → Média: 30.0`

---

## 🎯 **O que foi pedido**
Programa simples para treinar **arrays unidimensionais**:
1. Ler 3 idades do utilizador e guardar em `int[] idd = new int[3]`
2. Mostrar cada valor com posição "amigável" (1,2,3 ao invés de 0,1,2)
3. Calcular soma usando **acumulador**
4. Dividir pela quantidade de elementos (`.length`) para obter a média

## 🛠️ **Conceitos utilizados**

| Conceito | Uso no programa |
|----------|----------------|
| **Arrays** | `int[] idd = new int[3]` - declaração e inicialização |
| **Ciclo `for`** | 3 usos: entrada, saída e soma (mesma estrutura, propósitos diferentes) |
| **`Scanner`** | `ler.nextInt()` para capturar dados do teclado |
| **`.length`** | `idd.length` → 3 (quantidade de elementos) |
| **Acumulador** | `soma = idd[i] + soma` - soma iterativa |
| **Índices** | `(i + 1)` para exibição humana vs `i` para acesso real |

## 💡 **Detalhes técnicos importantes**


## 🎮 **Jogo do Galo (Tic-Tac-Toe)**
[![Ver Código](https://img.shields.io/badge/Ver_Código-Blue?style=for-the-badge&logo=github)](link-do-teu-codigo-java)

**O que foi pedido:** Implementar o **Jogo do Galo completo** em matriz 3x3 com turnos alternados (X/O), validação de jogadas e detecção automática de vencedor/empate.

### 🛠️ **Conceitos principais**
| Matrizes 2D | Métodos | Switch implícito | Validação | Recursão lógica | Scanner |

**Demo:** `Linha 1 Col 1 (X) → Linha 1 Col 2 (O) → 3 em linha → "X GANHOUUU!"`

---

## 🎯 **O que foi pedido**
Criar jogo completo do **Galo** (3x3) com:
1. Tabuleiro visual formatado com bordas (`| X | O | |`)
2. Turnos alternados (ímpar=X, par=O)  
3. Validação de posições ocupadas
4. Detecção automática de **vencedor** (linhas/colunas/diagonais)
5. **Empate** quando tabuleiro cheio
6. Interface interativa (coordenadas 0-2)

## 🛠️ **Conceitos utilizados**

| Conceito | Uso no programa |
|----------|----------------|
| **Matriz 2D** | `char mat[][] = new char[3][3]` - tabuleiro 3x3 |
| **Métodos** | 7 funções especializadas (verificaFim, mostramat, preenchemat, etc.) |
| **Arrays multidim.** | `mat[i][j]` - acesso coordenadas linha/coluna |
| **Lógica vitória** | 8 condições OR (3 linhas + 3 colunas + 2 diagonais) |
| **Controlo fluxo** | `while(jogada <= 9)` + `if(termina == -1)` para vitória |
| **Validação** | `verificaMat()` evita sobrescrita de posições ocupadas |

## 💡 **Detalhes técnicos importantes**
