a. Liste os números de todos os empregados, os seus nomes e números dos seus
chefes.

SELECT EMPNUM, NOME, CHEFE
FROM EMPREGADO;

b. Considerando que o salário é o salário anual, liste o salário mensal de cada
empregado.

SELECT EMPNUM, NOME, ROUND(SALARIO/12,2) AS SALARIO_MENSAL
FROM EMPREGADO;

c. Liste os departamentos existentes na empresa.

SELECT DISTINCT DEPNUM
FROM EMPREGADO
ORDER BY DEPNUM;

d. Liste os nomes, função e salário anual dos empregados da empresa, ordenados
alfabeticamente por nome.

SELECT NOME, FUNCAO, SALARIO, DEPNUM
FROM EMPREGADO
ORDER BY NOME ASC;

e. Liste todos empregados (numero, nome, função e numero de departamento) de todos
os Administrativos.

SELECT EMPNUM, NOME, FUNCAO, DEPNUM
FROM EMPREGADO
WHERE FUNCAO LIKE 'AD%';

f. Liste os empregados cujo salário anual é maior do que 20 000 €.

SELECT EMPNUM, NOME, SALARIO
FROM EMPREGADO
WHERE SALARIO>20000;

g. Liste os empregados cujo salário está entre 15000 e 20 000 €.

SELECT EMPNUM, NOME, SALARIO
FROM EMPREGADO 
WHERE SALARIO BETWEEN 15000 AND 20000;

h. Liste os empregados que sejam chefiados pelo no 33 e pelo no 39.

SELECT EMPNUM, NOME, CHEFE
FROM EMPREGADO
WHERE CHEFE = 33 
OR CHEFE = 39;


i. Liste todos os vendedores com salário maior que 16 000 €.

SELECT EMPNUM, NOME, FUNCAO, SALARIO  
FROM EMPREGADO
WHERE FUNCAO LIKE 'VEND%'
AND SALARIO > 16000;
