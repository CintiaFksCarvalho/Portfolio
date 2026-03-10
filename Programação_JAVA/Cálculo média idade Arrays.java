import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // Inicializa o objeto Scanner para capturar dados do teclado
        Scanner ler = new Scanner(System.in);

        // Variáveis de controlo e cálculo
        int i;
        float media, soma = 0;
        
        // Declaração do Array unidimensional de inteiros com 3 posições (índices 0, 1 e 2)
        int[] idd = new int[3];

        // 1ª PARTE: Entrada de dados (Ciclo de Preenchimento)
        // O ciclo percorre do índice 0 até o 2 (i < 3)
        for (i = 0; i < 3; i++) {
            // (i + 1) é usado apenas para mostrar "Idade 1" em vez de "Idade 0" ao utilizador
            System.out.println("Digite a idade " + (i + 1) + ": ");
            
            // O valor é guardado no índice real do array (começando em 0)
            idd[i] = ler.nextInt();
        }

        // 2ª PARTE: Exibição dos dados (Saída Formatada)
        System.out.println("\n--- Lista de Idades Inseridas ---");
        for (i = 0; i < 3; i++) {
            // Mantemos a lógica de mostrar a posição começando em 1 para facilitar a leitura humana
            // O acesso ao valor real usa o índice i (0, 1, 2)
            System.out.println("Posicao " + (i + 1) + ": " + idd[i]);
        }

        // 3ª PARTE: Processamento da Soma (Acumulador)
        // Percorremos o array novamente para somar todos os valores guardados
        for (i = 0; i < 3; i++) {
            soma = idd[i] + soma; // soma recebe o seu valor anterior + o valor atual do array
        }

        // Cálculo da média: divide-se o total somado pelo número de elementos (.length)
        media = soma / idd.length;
        
        // Exibição do resultado final formatado
        System.out.println("\nA media das idades e: " + media);
    }
}