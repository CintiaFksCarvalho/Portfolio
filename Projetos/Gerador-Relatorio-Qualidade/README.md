# Gerador de Relatórios de Qualidade Industrial

## 1. Sobre o projeto

Aplicação desenvolvida em Python para automatizar o tratamento de dados de qualidade industrial exportados de um sistema, transformando ficheiros Excel em relatórios estruturados para facilitar a análise de defeitos e o acompanhamento das unidades produtivas.

## 2. Problema identificado

Os ficheiros exportados pelo sistema de qualidade continham informações que necessitavam de tratamento, reorganização e consolidação.
A estrutura dos dados dificultava a consulta dos registos de peças não conformes, a análise dos defeitos e a identificação das referências e unidades produtivas com maior incidência.

## 3. Solução proposta

A partir da necessidade identificada, foi definida uma solução para automatizar o tratamento dos dados e gerar relatórios de qualidade organizados.
A aplicação permite importar ficheiros Excel, relacionar referências de artigos com unidades produtivas, processar os registos e gerar um novo ficheiro Excel com tabelas consolidadas, indicadores percentuais e rankings de defeitos.

## 4. Principais funcionalidades

- Importação de ficheiros Excel.
- Tratamento e organização automática dos dados.
- Associação de artigos às unidades produtivas.
- Consolidação de informações por artigo e unidade produtiva.
- Cálculo de indicadores de qualidade: BPC, PNC e PAD.
- Ranking dos três artigos com maior quantidade por tipo de defeito.
- Geração automática de relatórios Excel.
- Menu de navegação entre as diferentes folhas do relatório.

## 5. Participação na análise e definição da solução

A empresa apresentou a necessidade de melhorar a organização e a análise dos dados de qualidade industrial.
A minha participação começou pela análise dos ficheiros exportados pelo sistema, identificando os campos relevantes, as informações necessárias e as dificuldades existentes no processo de consulta e análise.
Com base nessa análise, realizei o levantamento e a organização dos requisitos funcionais, definindo:

- Os dados que deveriam ser considerados no tratamento.
- Os critérios de associação entre referências de artigos e unidades produtivas.
- As regras de organização e consolidação dos registos.
- Os indicadores de qualidade a apresentar.
- A estrutura e as informações esperadas nos relatórios.
- Os critérios para identificação e classificação dos artigos com maior quantidade de defeitos.

## 6. Tecnologias utilizadas e processo de desenvolvimento

**Tecnologias e ferramentas:**
- **Python:** linguagem utilizada na implementação da aplicação.
- **Pandas:** biblioteca utilizada para tratamento e organização de dados.
- **OpenPyXL:** biblioteca utilizada para manipulação e geração de ficheiros Excel.
- **Tkinter:** biblioteca utilizada na construção da interface gráfica.
- **Microsoft Excel:** ficheiros de entrada e relatórios gerados.
- **Gemini e Claude:** ferramentas de Inteligência Artificial utilizadas para a geração do código e implementação técnica da aplicação.

### Utilização de Inteligência Artificial

Todo o código da aplicação foi gerado com recurso às ferramentas de Inteligência Artificial Gemini e Claude.
A minha participação concentrou-se na análise da necessidade apresentada pela empresa, no levantamento e organização dos requisitos funcionais, na definição das regras de tratamento dos dados e na especificação dos resultados esperados.
A implementação foi orientada através de instruções contextualizadas, com apresentação dos requisitos, funcionalidades e comportamento esperado da aplicação. As soluções geradas foram analisadas e submetidas a testes e ajustes sucessivos, de forma a verificar a correspondência entre o funcionamento da aplicação e as necessidades identificadas.

## 7. Competências aplicadas

Análise de Processos | Levantamento de Requisitos | Análise Funcional | Regras de Negócio | Análise e Organização de Dados | Definição de Indicadores | Especificação Funcional | Testes e Validação | Utilização de IA no Desenvolvimento de Soluções.

## 8. Demonstração

As pastas `Demonstracao` e `Exemplos` contêm capturas de ecrã e ficheiros fictícios para apresentar o funcionamento da aplicação e os resultados gerados.

**Nota:** os ficheiros disponibilizados destinam-se exclusivamente à demonstração e utilizam dados fictícios. O código-fonte original e os dados internos da empresa não são disponibilizados.