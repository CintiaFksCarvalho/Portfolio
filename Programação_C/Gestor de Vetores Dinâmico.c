#include <stdio.h>


// --- FUNÇÕES DE ENTRADA E SAÍDA (I/O) ---

/**
 * Preenche o vetor. O uso do asterisco (*v) indica que estamos 
 * a passar o endereço de memória do vetor (ponteiro).
 */
void lerValores(float *v, int n) {
    printf("Introduza %d numeros:\n", n);
    for (int i = 0; i < n; i++) {
        printf("vetor[%d] = ", i);
        // O símbolo & indica o endereço da posição i do vetor
        scanf("%f", &v[i]);
    }
}

// Percorre o array e imprime os valores formatados com 2 casas decimais
void mostrarValores(float v[], int n) {
    printf("\nOs valores inseridos foram:\n");
    for (int i = 0; i < n; i++) {
        printf("vetor[%d] = %.2f\n", i, v[i]);
    }
}

/**
 * Altera um valor específico. Inclui um ciclo 'do-while' para 
 * validação de limites (impede acesso a índices inexistentes).
 */
void alterarValor(float v[], int n) {
    int i;
    printf("\nQual o indice a alterar (0-%d): ", n - 1);
    do {
        scanf("%d", &i);
        if (i < 0 || i >= n) {
            printf("Indice nao permitido! Tente novamente: ");
        }
    } while (i < 0 || i >= n);

    printf("Valor atual: %.2f\n", v[i]);
    printf("Novo valor: ");
    scanf("%f", &v[i]);
    printf("Valor atualizado com sucesso!\n");
}

// --- FUNÇÕES DE PROCESSAMENTO ---

// Calcula a somatória simples de todos os elementos
float calcularSoma(float v[], int n) {
    float soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }
    return soma;
}

/**
 * Calcula a média aritmética.
 * Reutiliza a função calcularSoma para evitar repetição de código (DRY - Don't Repeat Yourself).
 */
float calcularMedia(float v[], int n) {
    if (n == 0) return 0;
    return calcularSoma(v, n) / n;
}

// Algoritmo de busca para encontrar o maior elemento
float calculoMaximo(float *v, int n) {
    float maximo = v[0]; // Assume que o primeiro é o maior
    for (int i = 1; i < n; i++) {
        if (v[i] > maximo) maximo = v[i];
    }
    return maximo;
}

// Algoritmo de busca para encontrar o menor elemento
float calculoMinimo(float *v, int n) {
    float minimo = v[0]; // Assume que o primeiro é o menor
    for (int i = 1; i < n; i++) {
        if (v[i] < minimo) minimo = v[i];
    }
    return minimo;
}

// --- INTERFACE DE UTILIZADOR (UX) ---

int menu() {
    int op;
    printf("\n---------- MENU PRINCIPAL ----------\n");
    printf("1 - Inserir valores\n");
    printf("2 - Mostrar valores\n");
    printf("3 - Calcular estatisticas (Submenu)\n");
    printf("4 - Alterar valor especifico\n");
    printf("0 - Sair\n");
    printf("Escolha uma opcao: ");
    scanf("%d", &op);
    return op;
}

int submenu() {
    int op;
    printf("\n--- OPERACOES DISPONIVEIS ---\n");
    printf("1 - Soma\n");
    printf("2 - Media\n");
    printf("3 - Maximo\n");
    printf("4 - Minimo\n");
    printf("0 - Voltar ao Menu Principal\n");
    printf("Escolha uma opcao: ");
    scanf("%d", &op);
    return op;
}

// --- FLUXO PRINCIPAL ---

int main() {
    int inserido = 0; // Variável de controle (Flag) para validar se o vetor tem dados
    int tam, op, subop;

    printf("Defina o tamanho do vetor: ");
    scanf("%d", &tam);

    /**
     * Declaração de VLA (Variable Length Array). 
     * O tamanho é definido em tempo de execução conforme o input do usuário.
     */
    float vetor[tam];

    do {
        op = menu();

        switch (op) {
            case 1:
                lerValores(vetor, tam);
                inserido = 1; // Sinaliza que os dados foram carregados
                break;

            case 2:
                // Validação de estado: impede exibição de lixo de memória
                if (inserido) mostrarValores(vetor, tam);
                else printf("\n[ERRO] O vetor esta vazio. Use a opcao 1 primeiro.\n");
                break;

            case 3:
                if (inserido) {
                    float resultado = 0;
                    do {
                        subop = submenu();
                        // Menu aninhado (Submenu) para operações matemáticas
                        switch (subop) {
                            case 1: resultado = calcularSoma(vetor, tam); break;
                            case 2: resultado = calcularMedia(vetor, tam); break;
                            case 3: resultado = calculoMaximo(vetor, tam); break;
                            case 4: resultado = calculoMinimo(vetor, tam); break;
                            case 0: break;
                            default: printf("Opcao invalida!\n"); continue;
                        }
                        if (subop != 0) printf("\n>>> Resultado: %.2f\n", resultado);
                    } while (subop != 0);
                } else {
                    printf("\n[ERRO] Insira dados primeiro!\n");
                }
                break;

            case 4:
                if (inserido) alterarValor(vetor, tam);
                else printf("\n[ERRO] Insira dados primeiro!\n");
                break;

            case 0:
                printf("\nA encerrar o programa...\n");
                break;

            default:
                printf("\nOpcao inexistente!\n");
        }
    } while (op != 0);

    return 0;
}