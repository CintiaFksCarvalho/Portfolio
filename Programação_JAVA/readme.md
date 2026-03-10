# Programação em JAVA

## Cálculo de Média com Arrays

**<h3>[Ver código completo](https://github.com/CintiaFksCarvalho/Portfolio/blob/main/Programa%C3%A7%C3%A3o_JAVA/C%C3%A1lculo%20m%C3%A9dia%20idade%20Arrays.java)</h3>**

## O que foi pedido
Programa simples para treinar **arrays unidimensionais**:
- Ler 3 idades do utilizador e guardar em `int[] idd = new int[3]`
- Mostrar cada valor com posição "amigável" (1,2,3 ao invés de 0,1,2)
- Calcular soma usando **acumulador**
- Dividir pela quantidade de elementos (`.length`) para obter a média

## Conceitos utilizados

| Conceito | Uso no programa |
|----------|----------------|
| **Arrays** | `int[] idd = new int[3]` - declaração e inicialização |
| **Ciclo `for`** | 3 usos: entrada, saída e soma (mesma estrutura, propósitos diferentes) |
| **`Scanner`** | `ler.nextInt()` para capturar dados do teclado |
| **`.length`** | `idd.length` → 3 (quantidade de elementos) |
| **Acumulador** | `soma = idd[i] + soma` - soma iterativa |
| **Índices** | `(i + 1)` para exibição humana vs `i` para acesso real |


## Jogo do Galo (Tic-Tac-Toe)
**<h3>[Ver código completo](https://github.com/CintiaFksCarvalho/Portfolio/blob/main/Programa%C3%A7%C3%A3o_JAVA/Jogo%20Galo%20Arrays.java)</h3>**

## O que foi pedido
Criar jogo completo do **Galo** (3x3) com:
- Tabuleiro visual formatado com bordas (`| X | O | |`)
- Turnos alternados (ímpar=X, par=O)  
- Validação de posições ocupadas
- Detecção automática de **vencedor** (linhas/colunas/diagonais)
- **Empate** quando tabuleiro cheio
- Interface interativa (coordenadas 0-2)

## Conceitos utilizados

| Conceito | Uso no programa |
|----------|----------------|
| **Matriz 2D** | `char mat[][] = new char[3][3]` - tabuleiro 3x3 |
| **Métodos** | 7 funções especializadas (verificaFim, mostramat, preenchemat, etc.) |
| **Arrays multidim.** | `mat[i][j]` - acesso coordenadas linha/coluna |
| **Lógica vitória** | 8 condições OR (3 linhas + 3 colunas + 2 diagonais) |
| **Controlo fluxo** | `while(jogada <= 9)` + `if(termina == -1)` para vitória |
| **Validação** | `verificaMat()` evita sobrescrita de posições ocupadas |
