Faça atualizações aos registos.

a. O Presidente passou a ganhar uma comissão de 1000 €.

UPDATE EMPREGADO
SET COMISSAO = 1000
WHERE EMPNUM = 79;

b. Os Vendedores com uma comissão inferior a 2000 € passam a ganhar mais 300 €.

UPDATE EMPREGADO 
SET SALARIO = SALARIO + 300
WHERE COMISSAO < 2000
AND FUNCAO LIKE 'VENDEDOR'; 

c. O empregado Lima agora tem a função de Analista e passou a trabalhar no
departamento 40. Agora o seu chefe é o chefe do departamento 40.

UPDATE EMPREGADO 
SET FUNCAO = 'ANALISTA', 
    DEPNUM = 40, 
    CHEFE = 39
WHERE EMPNUM = 14;

d. Todos os Chefes passaram a ganhar mais 200 € de salário.

UPDATE EMPREGADO 
SET SALARIO = SALARIO + 200
WHERE FUNCAO LIKE 'CHEFE';

e. Atualizar todos os empregados do departamento 10 que não recebem comissão. Estes passam a ganhar mais 500€ de salario.

UPDATE EMPREGADO 
SET SALARIO = SALARIO + 500
WHERE DEPNUM = 10
AND COMISSAO IS NULL;  

f. Todos os empregados cujo nome comece pela letra A passam a ganhar mais 50€ de salário.

UPDATE EMPREGADO
SET SALARIO = SALARIO + 50
WHERE NOME LIKE 'A%';
