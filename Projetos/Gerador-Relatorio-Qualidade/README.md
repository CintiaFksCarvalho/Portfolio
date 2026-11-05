# Gerador de Relatórios de Qualidade Industrial

## 1. Sobre o projeto

Aplicação desenvolvida em Python para automatizar o tratamento de dados de qualidade industrial exportados de um sistema, transformando ficheiros Excel em relatórios estruturados para facilitar a análise de defeitos e o acompanhamento das unidades produtivas.

## 2. Problema identificado

Os ficheiros exportados pelo sistema apresentavam informações que necessitavam de reorganização e consolidação para facilitar a consulta e análise dos registos de peças não conformes.

## 3. Solução desenvolvida

Foi desenvolvida uma aplicação com interface gráfica que permite importar ficheiros Excel, relacionar referências de artigos com unidades produtivas, processar os dados e gerar automaticamente um novo ficheiro Excel com tabelas consolidadas, indicadores percentuais e rankings de defeitos.

## 4. Principais funcionalidades

- Importação de ficheiros Excel.
- Tratamento e organização automática dos dados.
- Associação de artigos às unidades produtivas.
- Consolidação de informações por artigo e unidade produtiva.
- Cálculo de indicadores de qualidade: BPC, PNC e PAD.
- Ranking dos três artigos com maior quantidade por tipo de defeito.
- Geração automática de relatórios Excel.
- Menu de navegação entre as diferentes folhas do relatório.

## 5. Tecnologias utilizadas

- Python
- Pandas
- OpenPyXL
- Tkinter
- Microsoft Excel

## 6. Processo de desenvolvimento

O desenvolvimento começou com a análise do ficheiro exportado pelo sistema de qualidade, identificando os campos relevantes e as informações necessárias para a análise operacional.

Foram definidas as regras de tratamento, associação dos artigos às unidades produtivas e consolidação dos indicadores.

Gemini e Claude foram utilizados como ferramentas de apoio à pesquisa, implementação técnica e resolução de problemas. As sugestões foram analisadas, adaptadas e testadas de acordo com os requisitos definidos para a aplicação.

## 7. Demonstração

As pastas `Demonstracao` e `Exemplos` contêm capturas de ecrã e ficheiros fictícios para apresentar o funcionamento e os resultados da aplicação.

**Nota:** Os ficheiros disponibilizados destinam-se exclusivamente à demonstração e utilizam dados fictícios. O código-fonte original e os dados internos da empresa não são disponibilizados.