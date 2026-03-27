# ETL Futebol - Pipeline de Dados

## Descrição

Este projeto implementa um pipeline completo de dados (ETL) utilizando informações de partidas de futebol obtidas via API pública.

Além do ETL, o projeto evoluiu para incluir:

* Persistência em banco de dados (MySQL)
* Análises estatísticas (ranking de times)
* Dashboard interativo com visualização de dados
* Automação do pipeline completo

Este projeto faz parte do meu aprendizado em **Engenharia de Dados e Análise de Dados**.

---

## Conceitos aplicados

* ETL (Extract, Transform, Load)
* Consumo de API REST
* Modelagem de dados
* Manipulação de JSON
* SQL (MySQL)
* Análise de dados
* Data Visualization
* Pipeline automatizado

---

## Tecnologias utilizadas

* Python
* Requests
* JSON
* MySQL
* Pandas
* Streamlit
* Git & GitHub

---

## Pipeline de Dados

### 1. Extract

Coleta de dados da API de futebol:

* Times
* Placar
* Data dos jogos
* Informações gerais da partida

---

### 2. Transform

Tratamento e organização dos dados:

* Seleção de campos relevantes
* Padronização dos dados
* Estruturação para análise

---

### 3. Load

Persistência dos dados:

* Banco de dados MySQL (`jogos`)
* Arquivos JSON

---

### 4. Analysis

Geração de métricas por time:

* Total de gols feitos
* Total de gols sofridos
* Saldo de gols
* Ranking geral

Critérios de ordenação:

1. Maior saldo de gols
2. Maior número de gols feitos
3. Menor número de gols sofridos

---

### 5. Dashboard

Visualização dos dados com Streamlit:

* Tabela de ranking com posição
* Melhor time (destaque)
* Melhor ataque
* Melhor defesa
* Cores por desempenho:

  * Verde → topo
  * Amarelo → meio
  * Vermelho → parte inferior

---

## Estrutura do Projeto

```
ProjetoEtl_Futebol/
│
├── analysis.py
├── dashboard.py
├── main.py
│
├── dados/
│   ├── jogos.json
│   └── jogos_tratados.json
│   └── ranking.json
│
├── etl/
│   ├── extract.py
│   └── transform.py
│   └── load.py
│
├── README.md
```

---

## Como executar

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd ProjetoEtl_Futebol
```

---

### 2. Execute o pipeline completo e inicia o dashboard

```bash
python main.py
```

---

## Automação

O arquivo `main.py` executa todo o pipeline automaticamente:

1. Extração
2. Transformação
3. Carga
4. Análise
5. Preparação dos dados para visualização
6. Visualização dos dados via dashboard

---

## Observação

Este projeto foi desenvolvido como parte do meu aprendizado em Engenharia de Dados, com foco em:

* Construção de pipelines completos
* Integração com banco de dados
* Análise e visualização de dados
* Organização e boas práticas de código
