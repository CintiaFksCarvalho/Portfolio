import java.util.Scanner;

public class Main {

    /**
     * Verifica se o jogador atual (c) completou uma linha, coluna ou diagonal.
     * Retorna 1 se houver um vencedor, 0 caso contrário.
     */
    public static int verificaFim(char mat[][], char c){
        // Verifica as 3 linhas, 3 colunas e as 2 diagonais comparando com o caractere 'c'
        if (mat[0][0] == c && mat[0][1] == c && mat [0][2]== c || 
            mat[1][0] == c && mat[1][1] == c && mat [1][2]== c || 
            mat[2][0] == c && mat[2][1] == c && mat [2][2]== c || 
            mat[0][0] == c && mat[1][0] == c && mat [2][0]== c || 
            mat[0][1] == c && mat[1][1] == c && mat [2][1]== c || 
            mat[0][2] == c && mat[1][2] == c && mat [2][2]== c ||
            mat[0][0] == c && mat[1][1] == c && mat [2][2]== c ||
            mat[0][2] == c && mat[1][1] == c && mat [2][0]== c){                   
                return 1;       
        }
        return 0;
    }
    
    /**
     * Percorre a matriz e imprime o tabuleiro formatado com barras laterais.
     */
    public static void mostramat(char m [][]){
        int i, j;
        for(i=0; i<m.length; i++){
            System.out.print("|");
            for(j=0; j<m.length; j++){
                System.out.print(m [i][j] + "|");
            }
            System.out.println(""); // Quebra de linha após cada linha da matriz
        }
    }
    
    /**
     * Insere 'X' ou 'O' na matriz com base no número da jogada (ímpar = X, par = O).
     * Verifica se a jogada resultou em vitória.
     */
    public static int preenchemat(char m [][], int l, int c, int jogada){
        int resto = jogada % 2;
        int fim;
        if (resto == 1){ // Jogadas 1, 3, 5, 7, 9 são do Jogador X
            m [l][c] = 'X';
            fim = verificaFim(m,'X');
            if(fim != 0){
                System.out.println("Terminou o Jogo, jogador X GANHOUUUU");
                return -1; // Retorno especial para indicar vitória
            }
        } else { // Jogadas 2, 4, 6, 8 são do Jogador O
            m [l][c] = 'O';
            fim = verificaFim(m,'O');
            if(fim != 0){
                System.out.println("Terminou o Jogo, Jogador O GANHOOOOU");
                return -1;
            }
        }
        return 1; // Jogo continua
    }
    
    /**
     * Valida se a posição escolhida está vazia (contém um espaço em branco).
     */
    public static int verificaMat(char m[][], int lin, int col){
        if(m[lin][col] == ' '){
            return 1; // Posição válida
        } else {
            return 0; // Posição já ocupada
        }
    }
    
    /**
     * Solicita um número inteiro ao utilizador (coordenadas).
     */
    public static int pedeInt(String st){
        Scanner ler = new Scanner (System.in);
        System.out.println(st);
        return ler.nextInt();
    }
    
    /**
     * Preenche todas as posições da matriz com espaços em branco (inicialização).
     */
    public static void preenchetab(char m [][]){
        for(int i=0; i<m.length; i++){
            for(int j=0; j<m.length; j++){
                m [i][j] = ' ';
            }
        }
    }
    
    /**
     * Gerencia o fluxo principal do jogo: turnos, entradas e condições de empate.
     */
    public static void tabuleiro( ){
        char [][] mat = new char [3][3];  
        System.out.println("--- Jogo do Galo ---");
        preenchetab(mat);
        mostramat(mat);
        
        int l, c, verif, termina;
        int jogada = 1;

        // O jogo tem no máximo 9 jogadas
        while (jogada <= 9){
            l = pedeInt("Indique a linha (0-2): ");
            c = pedeInt("Indique a coluna (0-2): ");
            
            // Valida se a posição está livre
            verif = verificaMat(mat, l, c);
            
            if (verif == 1){
                termina = preenchemat(mat, l, c, jogada);
                mostramat(mat);
                
                if(termina == -1){
                    jogada = 20; // Força a saída do loop pois houve um vencedor
                } else {
                    jogada++;
                }
            } else {
                System.out.println("Posicao ocupada! Escolha outra coordenada.");
            }
        }
        
        // Se o loop terminou em 10, significa que as 9 casas foram preenchidas sem vencedor
        if(jogada == 10){
             System.out.println("O jogo empatou (Velha)!");
        }
    }
    
    public static void main(String[] args) {
        tabuleiro(); // Inicia a execução
    }
}