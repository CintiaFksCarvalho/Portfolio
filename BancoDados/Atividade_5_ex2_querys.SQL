CREATE DATABASE atividade5ex2;

USE atividade5ex2;

CREATE TABLE Cliente
(id int,
 nome varchar(70),
 nif int(9),
 nss bigint,
 PRIMARY KEY(id));

CREATE TABLE Produto
(ref varchar(4),
 nome varchar(50),
 preco float(10),
 PRIMARY KEY(ref));

CREATE TABLE Fatura
(numfatura int,
 data date,
 id_cliente_fk int,
 PRIMARY KEY(numfatura),
 FOREIGN KEY(id_cliente_fk) REFERENCES Cliente(id));

CREATE TABLE Linha_Fatura
(idlf int,
 numfatura_fk int,
 ref_fk varchar(4),
 quantidade int,
 PRIMARY KEY(idlf),
 FOREIGN KEY(numfatura_fk) REFERENCES Fatura(numfatura),
 FOREIGN KEY(ref_fk) REFERENCES Produto(ref));


INSERT INTO Cliente(id, nome, nif, nss) VALUES(1, 'Rui Silva', 224863128, 12045632589);
INSERT INTO Cliente(id, nome, nif, nss) VALUES(2, 'Manuel Damião', 204586235, 12247634569);
INSERT INTO Cliente(id, nome, nif, nss) VALUES(3, 'Gabriela Batista', 215638456, 12354896357);
INSERT INTO Cliente(id, nome, nif, nss) VALUES(4, 'João Rafael', 235648759, 12458665523);
INSERT INTO Cliente(id, nome, nif, nss) VALUES(5, 'Anabela Vicente', 224796354, 12055699745);

INSERT INTO Produto(ref, nome, preco) VALUES('1A23', 'Incógnito Tinto', 25.50);
INSERT INTO Produto(ref, nome, preco) VALUES('5BC8', 'Malhadinha Tinto', 15.99);
INSERT INTO Produto(ref, nome, preco) VALUES('8AAG', 'Peceguina Tinto', 10.00);
INSERT INTO Produto(ref, nome, preco) VALUES('3FG2', 'V. Tinto Papa Figos', 7.50);

INSERT INTO Fatura(numfatura, data, id_cliente_fk) VALUES(1, '2008-10-16', 3);
INSERT INTO Fatura(numfatura, data, id_cliente_fk) VALUES(2, '2008-11-05', 2);
INSERT INTO Fatura(numfatura, data, id_cliente_fk) VALUES(3, '2016-10-06', 3);
INSERT INTO Fatura(numfatura, data, id_cliente_fk) VALUES(4, '2015-09-01', 1);

INSERT INTO Linha_Fatura(idlf, numfatura_fk, ref_fk, quantidade) VALUES(1, 1, '5BC8', 6);
INSERT INTO Linha_Fatura(idlf, numfatura_fk, ref_fk, quantidade) VALUES(2, 1, '1A23', 6);
INSERT INTO Linha_Fatura(idlf, numfatura_fk, ref_fk, quantidade) VALUES(3, 2, '8AAG', 12);
INSERT INTO Linha_Fatura(idlf, numfatura_fk, ref_fk, quantidade) VALUES(4, 3, '3FG2', 6);
INSERT INTO Linha_Fatura(idlf, numfatura_fk, ref_fk, quantidade) VALUES(5, 4, '1A23', 18);

a. Qual o NIF do cliente João Rafael?

SELECT C.NIF AS NIF_CLIENTE_JOÃO 
FROM CLIENTE C 
WHERE C.NOME LIKE 'JOÃO RAFAEL';

b. Qual o nome do produto mais caro?

SELECT MAX(P.PRECO) AS NOME_PRODUTO_CARO 
FROM PRODUTO P  
WHERE P.REF;

c. Qual o total faturado relativamente à cliente Gabriela Batista?

SELECT SUM(P.PRECO * LF.QUANTIDADE) AS TOTAL_FATURADO  
FROM PRODUTO P, FATURA F, CLIENTE C, LINHA_FATURA LF  
WHERE C.ID = F.ID_CLIENTE_FK
AND F.NUMFATURA = LF.NUMFATURA_FK
AND LF.REF_FK = P.REF
AND C.NOME LIKE 'GABRIELA BATISTA';

d. Quantas unidades de Incógnito Tinto já foram vendidas?

SELECT SUM(LF.QUANTIDADE) AS TOTAL_VENDIDO_INCOGNITO
FROM PRODUTO P, LINHA_FATURA LF
WHERE P.NOME LIKE 'INCOGNITO TINTO'
AND P.REF = LF.REF_FK;

e. Que produtos foram vendidos no dia 2008-11-05 e quem os comprou?

SELECT P.NOME, C.NOME
FROM PRODUTO P, FATURA F, CLIENTE C, LINHA_FATURA LF  
WHERE C.ID = F.ID_CLIENTE_FK
AND F.NUMFATURA = LF.NUMFATURA_FK
AND LF.REF_FK = P.REF
AND F.DATA LIKE '2008-11-05';
