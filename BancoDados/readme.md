# Exercícios de Bases de Dados

Atividades práticas do curso Técnico de Informática – Sistemas. Foco em SQL: criação de tabelas, INSERT, SELECT, GROUP BY, JOIN, UPDATE.

## Projetos

### 1. **atividade-empresa.sql**  
**O que foi feito:** Criação da base de dados `EMPRESA` com tabela `EMPREGADO` (campos: EMPNUM, NOME, FUNCAO, CHEFE, DATA_ADM, SALARIO, COMISSAO, DEPNUM). Inserção de 19 registos de funcionários.  
**Conceitos:** CREATE TABLE, PRIMARY KEY, INSERT múltiplo.  
👉 [Ver código](./atividade-empresa.sql)

### 2. **atividade-4-empresa-empregado.sql**  
**O que foi feito:** Consultas agregadas na tabela EMPREGADO: médias de salário, mínimos por função, contagens por departamento, GROUP BY, HAVING, filtros com WHERE.  
**Conceitos:** AVG, MIN, COUNT, GROUP BY, HAVING.  
👉 [Ver código](./atividade-4-empresa-empregado.sql)

### 3. **EMPRESA-EMPREGADO-UPDATE.SQL**  
**O que foi feito:** Consultas básicas: listagens com ORDER BY, filtros WHERE, BETWEEN, IN, LIKE para funções/salários.  
**Conceitos:** SELECT básico, DISTINCT, ORDER BY, LIKE, BETWEEN, IN.  
👉 [Ver código](./EMPRESA-EMPREGADO-UPDATE.SQL)

### 4. **EMPRESA-ATUALIZACOES.SQL**  
**O que foi feito:** Atualizações condicionais na tabela EMPREGADO: UPDATE com SET, WHERE complexo (filtro por função, comissão, nome, etc.).  
**Conceitos:** UPDATE, LIKE, IS NULL.  
👉 [Ver código](./EMPRESA-ATUALIZACOES.SQL)

### 5. **atividade-5-ex1-JUNCAO.SQL**  
**O que foi feito:** Base `atividade5ex1` com tabelas Localidade, Cliente, Telefone. Inserções e consultas com JOIN implícito para contagens e filtros.  
**Conceitos:** FOREIGN KEY, JOIN implícito (WHERE), COUNT com múltiplas tabelas.  
👉 [Ver código](./Atividade_5_ex1-JUNCAO.SQL)

### 6. **atividade-5-ex2.sql** e **atividade-5-ex2-1.sql**  
**O que foi feito:** Base `atividade5ex2` com tabelas Cliente, Produto, Fatura, Linha_Fatura (chaves estrangeiras). Inserções e consultas complexas: total faturado, SUM com multiplicação, JOIN múltiplas tabelas.  
**Conceitos:** FOREIGN KEY, JOIN múltiplo, SUM, GROUP BY, LIKE.  
👉 [Completo](./Atividade_5_ex2.SQL) | [Dados base](./Atividade_5_ex2-1.SQL)

### 7. **TRANSPORTADORA_AVIAO.SQL**  
**O que foi feito:** Base `TRANSPORTADORA_AVIAO` com 7 tabelas (Aviao, Telemovel, Morada, Piloto, Voo, Voo_Piloto, Piloto_Telemovel). Estrutura relacional completa com AUTO_INCREMENT, UNIQUE, múltiplas FK e tabelas de junção.  
**Conceitos:** Design de BD relacional, PRIMARY KEY, FOREIGN KEY, tabelas de ligação (many-to-many).  
👉 [Ver código](./TRANSPORTADORA_AVIAO.SQL)

---

**Competências demonstradas:** Modelagem de bases de dados, consultas agregadas (AVG, COUNT, SUM, MIN/MAX), JOINs, UPDATEs condicionais, criação de tabelas com relacionamentos.
