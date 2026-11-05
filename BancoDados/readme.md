# Bases de Dados — Exercícios de SQL

Atividades práticas realizadas durante a formação de Técnico de Informática – Sistemas, Nível 4, com foco na criação e gestão de bases de dados relacionais, manipulação de registos e elaboração de consultas SQL.

---

## 01. Criação de Bases de Dados e Inserção de Registos

**Ficheiro:** `Atividade_empresa_empregado_insert.SQL`

**Objetivo:** Criar uma base de dados denominada `EMPRESA`, estruturar a tabela `EMPREGADO` e inserir registos de funcionários.

**Atividades realizadas:**
- Criação da base de dados.
- Criação da tabela `EMPREGADO`.
- Definição de chave primária (`PRIMARY KEY`).
- Inserção de múltiplos registos.
- Utilização de valores `NULL`.

**Conceitos aplicados:** `CREATE DATABASE` | `CREATE TABLE` | `PRIMARY KEY` | `INSERT INTO` | `NULL`.

[Consultar código SQL](https://github.com/CintiaFksCarvalho/Portfolio/blob/main/BancoDados/Atividade_empresa_empregado_insert.SQL)

---

## 02. Consultas e Filtragem de Dados

**Ficheiro:** `Atividade_empresa_empregado_update.SQL`

**Objetivo:** Realizar consultas para pesquisar, ordenar e filtrar informações da tabela `EMPREGADO`.

**Atividades realizadas:**
- Listagem de registos.
- Consulta de valores distintos.
- Ordenação de resultados.
- Filtragem com diferentes condições.
- Cálculo e apresentação de valores salariais mensais.

**Conceitos aplicados:** `SELECT` | `DISTINCT` | `ORDER BY` | `WHERE` | `LIKE` | `BETWEEN` | `IN` | `ROUND`.

[Consultar código SQL](https://github.com/Cintiafkscarvalho/Portfolio/blob/main/BancoDados/Atividade_empresa_empregado_update.SQL)

---

## 03. Consultas Agregadas e Agrupamento de Dados

**Ficheiro:** `Atividade_empregado_update.sql`

**Objetivo:** Realizar consultas para analisar informações de funcionários, agrupando registos e calculando indicadores por função e departamento.

**Atividades realizadas:**
- Cálculo de médias salariais.
- Identificação de valores mínimos e máximos.
- Contagem de funcionários.
- Agrupamento por função e departamento.
- Aplicação de condições sobre os grupos de resultados.

**Conceitos aplicados:** `AVG` | `MIN` | `MAX` | `COUNT` | `GROUP BY` | `HAVING` | `WHERE`.

[Consultar código SQL](https://github.com/Cintiafkscarvalho/Portfolio/blob/main/BancoDados/Atividade_empregado_update.sql)

---

## 04. Atualização de Registos

**Ficheiro:** `Atividade_empresa_update.SQL`

**Objetivo:** Atualizar informações de funcionários de acordo com diferentes critérios e condições.

**Atividades realizadas:**
- Atualização de dados por função.
- Alteração de informações relacionadas com comissões.
- Atualização de nomes e departamentos.
- Aplicação de condições para selecionar os registos a modificar.

**Conceitos aplicados:** `UPDATE` | `SET` | `WHERE` | `LIKE` | `IS NULL` | Operadores de comparação.

[Consultar código SQL](https://github.com/Cintiafkscarvalho/Portfolio/blob/main/BancoDados/Atividade_empresa_update.SQL)

---

## 05. Relacionamento entre Tabelas e Consultas com JOIN

**Ficheiro:** `Atividade_5_ex2_querys.SQL`

**Objetivo:** Criar uma base de dados relacional para gerir informações de clientes, produtos, faturas e linhas de faturação, realizando consultas sobre os dados relacionados.

**Atividades realizadas:**
- Criação da base de dados `atividade5ex2`.
- Criação das tabelas `Cliente`, `Produto`, `Fatura` e `Linha_Fatura`.
- Definição de chaves estrangeiras (`FOREIGN KEY`).
- Inserção de dados nas diferentes tabelas.
- Consulta de informações de clientes e produtos.
- Identificação do produto com maior preço.
- Cálculo do total faturado por cliente.
- Consulta de quantidades vendidas e produtos associados a faturas e datas.

**Conceitos aplicados:** `CREATE TABLE` | `PRIMARY KEY` | `FOREIGN KEY` | `INSERT` | `SELECT` | `JOIN` | `SUM` | `MAX` | `LIKE` | Filtros por data.

[Consultar código SQL](https://github.com/Cintiafkscarvalho/Portfolio/blob/main/BancoDados/Atividade_5_ex2_querys.SQL)

---

## Competências técnicas

SQL | Bases de Dados Relacionais | Modelação Básica de Dados | Criação de Tabelas | Chaves Primárias e Estrangeiras | Inserção e Atualização de Registos | Consultas SQL | Filtragem e Ordenação | Funções de Agregação | GROUP BY | JOIN.