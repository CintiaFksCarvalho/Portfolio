#include <stdio.h>

// FUNÇÕES DE ENTRADA E SAÍDA

// Lê 'n' valores do utilizador e armazena no vetor v
void lerValores(float *v, int n) {
    printf("Introduza %d numeros:\\n", n);
    for (int i = 0; i < n; i++) {
        printf("vetor[%d] = ", i);
        scanf("%f", &v[i]);
    }
}

// Imprime todos os elementos do vetor com 2 casas decimais
void mostrarValores(float v[], int n) {
    printf("\\nOs valores inseridos foram:\\n");
    for (int i = 0; i < n; i++) {
        printf("vetor[%d] = %.2f\\n", i, v[i]);
    }
}

// Permite alterar um valor específico validando se o índice existe
void alterarValor(float v[], int n) {
    int i;
    printf("\\nQual o indice a alterar (0-%d): ", n - 1);
    do {
        scanf("%d", &i);
        if (i < 0 || i >= n) {
            printf("Indice nao permitido! Tente novamente: ");
        }
    } while (i < 0 || i >= n);

    printf("Valor atual: %.2f\\n", v[i]);
    printf("Novo valor: ");
    scanf("%f", &v[i]);
    printf("Valor atualizado com sucesso!\\n");
}

// FUNÇÕES DE PROCESSAMENTO

// Calcula a soma total dos elementos
float calcularSoma(float v[], int n) {
    float soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }
    return soma;
}

// Calcula a média (reutiliza a função de soma para eficiência)
float calcularMedia(float v[], int n) {
    if (n == 0) return 0;
    return calcularSoma(v, n) / n;
}

// Procura o maior valor no vetor
float calculoMaximo(float *v, int n) {
    float maximo = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] > maximo) maximo = v[i];
    }
    return maximo;
}

// Procura o menor valor no vetor
float calculoMinimo(float *v, int n) {
    float minimo = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < minimo) minimo = v[i];
    }
    return minimo;
}

// INTERFACE DE UTILIZADOR

int menu() {
    int op;
    printf("\\n---------- MENU PRINCIPAL ----------\\n");
    printf("1 - Inserir valores\\n");
    printf("2 - Mostrar valores\\n");
    printf("3 - Calcular estatisticas (Submenu)\\n");
    printf("4 - Alterar valor especifico\\n");
    printf("0 - Sair\\n");
    printf("Escolha uma opcao: ");
    scanf("%d", &op);
    return op;
}

int submenu() {
    int op;
    printf("\\n--- OPERACOES DISPONIVEIS ---\\n");
    printf("1 - Soma\\n");
    printf("2 - Media\\n");
    printf("3 - Maximo\\n");
    printf("4 - Minimo\\n");
    printf("0 - Voltar ao Menu Principal\\n");
    printf("Escolha uma opcao: ");
    scanf("%d", &op);
    return op;
}

// FLUXO PRINCIPAL

int main() {
    int inserido = 0; // Flag para verificar se o vetor já tem dados
    int tam, op, subop;

    printf("Defina o tamanho do vetor: ");
    scanf("%d", &tam);

    // Declaração de VLA (Variable Length Array)
    float vetor[tam];

    do {
        op = menu();

        switch (op) {
            case 1:
                lerValores(vetor, tam);
                inserido = 1; // Ativa a flag após a primeira leitura
                break;

            case 2:
                if (inserido) mostrarValores(vetor, tam);
                else printf("\\n[ERRO] O vetor esta vazio. Use a opcao 1 primeiro.\\n");
                break;

            case 3:
                if (inserido) {
                    float resultado = 0;
                    do {
                        subop = submenu();
                        switch (subop) {
                            case 1: resultado = calcularSoma(vetor, tam); break;
                            case 2: resultado = calcularMedia(vetor, tam); break;
                            case 3: resultado = calculoMaximo(vetor, tam); break;
                            case 4: resultado = calculoMinimo(vetor, tam); break;
                            case 0: break;
                            default: printf("Opcao invalida!\\n"); continue;
                        }
                        if (subop != 0) printf("\\n>>> Resultado: %.2f\\n", resultado);
                    } while (subop != 0);
                } else {
                    printf("\\n[ERRO] Insira dados primeiro!\\n");
                }
                break;

            case 4:
                if (inserido) alterarValor(vetor, tam);
                else printf("\\n[ERRO] Insira dados primeiro!\\n");
                break;

            case 0:
                printf("\\nA encerrar o programa...\\n");
                break;

            default:
                printf("\\nOpcao inexistente!\\n");
        }
    } while (op != 0);

    return 0;
}