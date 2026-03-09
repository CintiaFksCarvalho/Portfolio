#include <stdio.h>
#include <stdlib.h> 
#include <time.h>   

int main() {
    
    // Inicializa o gerador de números aleatórios com base no tempo atual
    srand(time(NULL)); 

    // Declaração de variáveis de configuração e estado
    int opc = 0;                     
    int max_tentativas = 5;          
    int limite_max_numero = 100;    
    int numero_secreto;              
    int palpite;                     
    int tentativa_atual;             
    int acertou = 0;                 
    printf("==================\\n");
    printf("BEM-VINDO AO JOGO!\\n"); 

    // Loop principal do sistema (Menu)
    do { 
        
        printf("=  MENU DO JOGO  =\\n");
        printf("==================\\n");
        printf("1- Jogar\\n");
        printf("2- Configurar limite de vezes\\n");
        printf("3- Configurar limite máximo do número\\n");
        printf("4- Ajuda\\n");
        printf("5- Sair do Programa\\n");
        printf("===================\\n");
        
        printf("Escolha uma opção: ");

        /**
         * Tratamento de Erro: Caso o usuário digite uma letra em vez de número,
         * o scanf falha. Este bloco limpa o buffer para evitar loops infinitos.
         */
        if (scanf("%d", &opc) != 1) { 
            opc = 0; 
            while(getchar() != '\\n'); 
        }
        
        switch(opc){
            case 1: // LÓGICA DO JOGO
                // Gera o número secreto entre 1 e o limite definido
                numero_secreto = (rand() % limite_max_numero) + 1; 
                tentativa_atual = 0;
                acertou = 0;
                
                printf("\\n--- JOGO INICIADO ---\\n");
                printf("Tente adivinhar o número entre 1 e %d. Você tem %d tentativas.\\n", limite_max_numero, max_tentativas);

                // Loop das tentativas do jogador
                while (tentativa_atual < max_tentativas) {
                    printf("\\nTentativa %d/%d. Digite seu palpite: ", tentativa_atual + 1, max_tentativas);
                    scanf("%d", &palpite);
                    
                    if (palpite == numero_secreto) {
                        printf("\\n!!! ACERTOU! Parabéns, você venceu !!!\\n");
                        acertou = 1;
                        break; 
                    } else if (palpite < numero_secreto) {
                        printf("ERROU: O número secreto e MAIOR que %d.\\n", palpite);
                    } else {
                        printf("ERROU: O número secreto e MENOR que %d.\\n", palpite);
                    }
                    
                    tentativa_atual++;
                }
                
                if (!acertou) {
                    printf("\\n--- FIM DE JOGO ---\\n");
                    printf("Acabaram as tentativas. O número secreto era %d.\\n", numero_secreto);
                }
                break; 
            
            case 2: // CONFIGURAÇÃO: TENTATIVAS
                printf("\\n--- CONFIGURAR NÚMERO DE TENTATIVAS ---\\n");
                printf("Digite o novo número máximo de tentativas: ");
                scanf("%d", &max_tentativas);
                
                // Validação para evitar números negativos ou zero
                if (max_tentativas <= 0) {
                    printf("Valor inválido. O mínimo e 1. Definindo para padrão (5).\\n");
                    max_tentativas = 5;
                } else {
                    printf("Novo limite de tentativas definido para: %d.\\n", max_tentativas);
                }
                break;
                
            case 3: // CONFIGURAÇÃO: DIFICULDADE
                printf("\\n--- CONFIGURAR LIMITE MÁXIMO DO NÚMERO SECRETO ---\\n");
                printf("Digite o novo limite máximo (ex: 1000): ");
                scanf("%d", &limite_max_numero); 
                
                if (limite_max_numero < 2) {
                    printf("O limite deve ser pelo menos 2. Definindo para 100.\\n");
                    limite_max_numero = 100;
                } else {
                    printf("Novo limite maximo definido para: %d.\\n", limite_max_numero);
                }
                break;
                
            case 4: // INFORMAÇÕES
                printf("\\n--- AJUDA DO JOGO ---\\n");
                printf("O objetivo e adivinhar o número secreto no menor número de tentativas.\\n");
                printf("Configurações atuais: %d Tentativas | Numero Maximo: %d.\\n", max_tentativas, limite_max_numero);
                break;
                
            case 5: // SAÍDA
                printf("\\nSaindo do programa. Até mais!\\n");
                break;
                
            default:
                printf("\\nOpção inválida. Tente novamente.\\n");
        }
        
    } while (opc != 5);

    return 0;
}