# Exercícios de Bases de Dados

Foco em SQL: criação de tabelas, INSERT, SELECT, GROUP BY, JOIN, UPDATE.

## Projetos

### 1. **Atividade_empresa_empregado_insert.SQL**  
**O que foi feito:** Criação da base `EMPRESA` e tabela `EMPREGADO`. Inserção de 19 registos de funcionários (admins, vendedores, chefes, presidente).  
**Conceitos:** CREATE DATABASE/TABLE, PRIMARY KEY, INSERT múltiplo com NULL.  
👉 [Ver código](https://github.com/CintiaFksCarvalho/Portfolio/blob/main/BancoDados/Atividade_empresa_empregado_insert.SQL)

### 2. **Atividade_empresa_empregado_update.SQL**  
**O que foi feito:** Consultas SELECT básicas e intermediárias: listagens, DISTINCT, ORDER BY, filtros com LIKE/BETWEEN/IN, salário mensal (ROUND).  
**Conceitos:** SELECT com ORDER BY, DISTINCT, WHERE complexo, funções matemáticas (ROUND).  
👉 [Ver código](https://github.com/CintiaFksCarvalho/Portfolio/blob/main/BancoDados/Atividade_empresa_empregado_update.SQL)

### 3. **Atividade_empregado_update.sql**  
**O que foi feito:** Consultas agregadas avançadas na tabela EMPREGADO: médias salariais por função/departamento, mínimos, contagens, GROUP BY múltiplo, HAVING, filtros.  
**Conceitos:** AVG/MIN/MAX/COUNT, GROUP BY com múltiplas colunas, HAVING COUNT > N.  
👉 [Ver código](https://github.com/CintiaFksCarvalho/Portfolio/blob/main/BancoDados/Atividade_empregado_update.sql)

### 4. **Atividade_empresa_update.SQL**  
**O que foi feito:** Atualizações múltiplas na tabela EMPREGADO: UPDATE condicional por função, comissão, nome, departamento.  
**Conceitos:** UPDATE com SET múltiplo, WHERE com LIKE, IS NULL, comparações.  
👉 [Ver código](https://github.com/CintiaFksCarvalho/Portfolio/blob/main/BancoDados/Atividade_empresa_update.SQL)

### 5. **Atividade_5_ex2_querys.SQL**  
**O que foi feito:** Criação completa da base `atividade5ex2` (Cliente, Produto, Fatura, Linha_Fatura com FK). Inserção de dados de clientes, vinhos, faturas. **Query's de análise:** NIF cliente específico, produto mais caro (MAX), total faturado por cliente (SUM com JOIN 4 tabelas), unidades vendidas de produto específico, produtos vendidos numa data com cliente.  
**Conceitos:** JOIN múltiplas tabelas (implícito), SUM(preço*quantidade), MAX, LIKE, filtros por data/nome.  
👉 [Ver código](https://github.com/CintiaFksCarvalho/Portfolio/blob/main/BancoDados/Atividade_5_ex2_querys.SQL)
