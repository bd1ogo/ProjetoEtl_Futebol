# ⚽ ETL Futebol - Pipeline de Dados

## 📌 Descrição

Este projeto tem como objetivo construir um pipeline de dados (ETL) utilizando dados de futebol obtidos através de uma API pública.

O pipeline realiza:

* Extração de dados de partidas de futebol
* Transformação dos dados em um formato estruturado
* Armazenamento em arquivo JSON (primeira etapa)

Este projeto faz parte do meu aprendizado na área de Engenharia de Dados.

---

## 🧠 Conceitos aplicados

* ETL (Extract, Transform, Load)
* Consumo de API REST
* Manipulação de JSON
* Estruturação de dados
* Organização de projeto

---

## ⚙️ Tecnologias utilizadas

* Python
* Requests
* JSON
* Git & GitHub

---

## 🔄 Pipeline de Dados

### 1. Extract

Coleta de dados da API de futebol:

* Endpoint: eventos de uma liga
* Dados retornados: times, placar, data, etc.

### 2. Transform

Tratamento dos dados:

* Seleção de campos relevantes
* Organização em estrutura JSON
* Preparação para persistência

### 3. Load

Armazenamento dos dados em:

* Arquivo JSON local (`data/jogos.json`)

---

## 📂 Estrutura do Projeto

```
ProjetoEtl_Futebol/
│
├── extract.py
├── data/
│   └── jogos.json
├── README.md
```

---

## ▶️ Como executar

1. Clone o repositório:

```
git clone <url-do-repositorio>
```

2. Acesse a pasta:

```
cd ProjetoEtl_Futebol
```

3. Execute o script:

```
python extract.py
```

---

## 🚀 Próximos passos

* Separar etapas em módulos (extract, transform, load)
* Persistir dados em banco MySQL
* Dockerizar o pipeline
* Automatizar execução
* Criar análises e dashboards

---

## 📌 Observação

Este projeto está em evolução contínua como parte do meu aprendizado em Engenharia de Dados.
