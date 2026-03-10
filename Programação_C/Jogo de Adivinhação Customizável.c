#include <stdio.h>
#include <stdlib.h> 
#include <time.h>   


int main() {
    
    /**
     * Inicializa a semente do gerador de números aleatórios.
     * time(NULL) fornece o tempo atual, garantindo que o número secreto 
     * mude a cada execução do programa.
     */
    srand(time(NULL)); 

    // Variáveis de estado e configuração inicial
    int opc = 0;                     // Opção escolhida no menu
    int max_tentativas = 5;          // Limite padrão de tentativas
    int limite_max_numero = 100;     // Range padrão (1 a 100)
    int numero_secreto;              // Número gerado pelo computador
    int palpite;                     // Entrada do usuário
    int tentativa_atual;             // Contador de tentativas
    int acertou = 0;                 // Flag de controle de vitória
    
    printf("==================\n");
    printf("BEM-VINDO AO JOGO!\n"); 

    // LOOP PRINCIPAL: Mantém o programa rodando até que a opção 5 (Sair) seja escolhida
    do { 
        printf("=  MENU DO JOGO  =\n");
        printf("==================\n");
        printf("1- Jogar\n");
        printf("2- Configurar limite de vezes\n");
        printf("3- Configurar limite máximo do número\n");
        printf("4- Ajuda\n");
        printf("5- Sair do Programa\n");
        printf("===================\n");
        
        printf("Escolha uma opção: ");

        /**
         * TRATAMENTO DE ERRO NO INPUT:
         * scanf retorna o número de itens lidos com sucesso.
         * Se o usuário digitar uma letra, scanf falha (!= 1).
         * O loop while(getchar()) limpa o "lixo" do buffer para evitar loops infinitos.
         */
        if (scanf("%d", &opc) != 1) { 
            opc = 0; 
            while(getchar() != '\n'); 
        }
        
        switch(opc){
            case 1: // --- LÓGICA DO JOGO ---
                // Gera número aleatório no intervalo configurado [1, limite_max_numero]
                numero_secreto = (rand() % limite_max_numero) + 1; 
                tentativa_atual = 0;
                acertou = 0;
                
                printf("\n--- JOGO INICIADO ---\n");
                printf("Tente adivinhar o número entre 1 e %d. Você tem %d tentativas.\n", limite_max_numero, max_tentativas);

                // Ciclo de tentativas do jogador
                while (tentativa_atual < max_tentativas) {
                    printf("\nTentativa %d/%d. Digite seu palpite: ", tentativa_atual + 1, max_tentativas);
                    scanf("%d", &palpite);
                    
                    if (palpite == numero_secreto) {
                        printf("\n!!! ACERTOU! Parabens, voce venceu !!!\n");
                        acertou = 1;
                        break; // Interrompe o loop de tentativas imediatamente
                    } else if (palpite < numero_secreto) {
                        printf("ERROU: O número secreto e MAIOR que %d.\n", palpite);
                    } else {
                        printf("ERROU: O número secreto e MENOR que %d.\n", palpite);
                    }
                    
                    tentativa_atual++;
                }
                
                // Verifica se o jogador perdeu por falta de tentativas
                if (!acertou) {
                    printf("\n--- FIM DE JOGO ---\n");
                    printf("Acabaram as tentativas. O número secreto era %d.\n\n", numero_secreto);
                }
                break; 
            
            case 2: // --- CONFIGURAÇÃO: TENTATIVAS ---
                printf("\n--- CONFIGURAR NúMERO DE TENTATIVAS ---\n");
                printf("Digite o novo número máximo de tentativas: ");
                scanf("%d", &max_tentativas);
                
                // Validação de sanidade: não permite jogos impossíveis (<= 0 tentativas)
                if (max_tentativas <= 0) {
                    printf("Valor inválido. O mínimo e 1. Definindo para padrão (5).\n");
                    max_tentativas = 5;
                } else {
                    printf("Novo limite de tentativas definido para: %d.\n\n", max_tentativas);
                }
                break;
                
            case 3: // --- CONFIGURAÇÃO: DIFICULDADE (RANGE) ---
                printf("\n--- CONFIGURAR LIMITE MAXIMO DO NÚMERO SECRETO ---\n");
                printf("Digite o novo limite máximo (ex: 1000): \n");
                scanf("%d", &limite_max_numero); 
                
                if (limite_max_numero < 2) {
                    printf("O limite deve ser pelo menos 2. Definindo para 100.\n\n");
                    limite_max_numero = 100;
                } else {
                    printf("Novo limite máximo definido para: %d.\n\n", limite_max_numero);
                }
                break;
                
            case 4: // --- INFORMAÇÕES/HELP ---
                printf("\n--- AJUDA DO JOGO ---\n");
                printf("O objetivo e adivinhar o número secreto no menor número de tentativas.\n");
                printf("Configurações atuais: %d Tentativas | Número Máximo: %d.\n", max_tentativas, limite_max_numero);
                break;
                
            case 5: // --- SAÍDA ---
                printf("\nSaindo do programa. Atá mais!\n");
                break;
                
            default:
                printf("\nOpção inválida. Tente novamente.\n");
        }
        
    } while (opc != 5);

    return 0;
}