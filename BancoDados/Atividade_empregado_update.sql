a. Calcule a média de salários de todos os empregados.

SELECT AVG(SALARIO) AS SALARIO_MEDIO
FROM EMPREGADO

--------------------------------------------

SELECT ROUND(AVG(SALARIO),2) AS SALARIO_MEDIO
FROM EMPREGADO;

b. Encontre o mínimo salário recebido por um empregado administrativo.

SELECT MIN(SALARIO) AS SALARIO_MENOR
FROM EMPREGADO 
WHERE FUNCAO LIKE 'ADMIN';

c. Quantos empregados tem o departamento 20?

SELECT COUNT(EMPNUM) AS NUM_EMP_DEP_20
FROM EMPREGADO 
WHERE DEPNUM = 20;

d. Calcule o salário médio para cada função.

SELECT FUNCAO, AVG(SALARIO) AS SALARIO_MEDIO
FROM EMPREGADO
GROUP BY FUNCAO;

e. Calcule o salário médio para cada função, excluindo o presidente.

SELECT FUNCAO, AVG(SALARIO) AS SALARIO_MEDIO
FROM EMPREGADO
WHERE FUNCAO NOT LIKE 'PRESIDENTE'
GROUP BY FUNCAO;

f. Encontre o salário médio para cada função dentro de cada departamento.

SELECT FUNCAO, DEPNUM, AVG(SALARIO) AS SALARIO_MEDIO
FROM EMPREGADO
GROUP BY FUNCAO, DEPNUM;

g. Encontre o salário mais baixo para cada departamento.

SELECT DEPNUM, MIN(SALARIO) AS SALARIO_MENOR_POR_DEP
FROM EMPREGADO 
GROUP BY DEPNUM;

h. Mostre o salário médio de cada departamento com mais de 4 pessoas.

SELECT DEPNUM, AVG(SALARIO) AS SALARIO_MEDIO
FROM EMPREGADO 
GROUP BY DEPNUM 
HAVING COUNT(EMPNUM) > 4;

i. Mostre apenas as funções cujo salário máximo é maior ou igual a 20 000 €.

SELECT FUNCAO, MAX(SALARIO) AS SALARIO_MAIOR
FROM EMPREGADO 
WHERE SALARIO >= 20000
GROUP BY FUNCAO;












































































































