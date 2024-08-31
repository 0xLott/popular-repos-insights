# Análise de Repositórios Populares de Código Aberto no GitHub

## 1. Introdução

Neste trabalho, foi realizada uma análise dos 1.000 repositórios mais populares do GitHub de acordo com o número de estrelas com o objetivo de avaliar suas características e padrões de desenvolvimento observados. Para isso, o estudo foi guiado a partir das seguintes perguntas de pesquisa (RQ, do inglês "Research Questions"):

- **RQ 01**: Sistemas populares são maduros/antigos?
- **RQ 02**: Sistemas populares recebem muita contribuição externa?
- **RQ 03**: Sistemas populares lançam releases com frequência?
- **RQ 04**: Sistemas populares são atualizados com frequência?
- **RQ 05**: Sistemas populares são escritos nas linguagens mais populares?
- **RQ 06**: Sistemas populares possuem um alto percentual de issues fechadas?

## 2. Hipóteses Informais

De forma preliminar, elaborou-se as seguintes hipóteses informais para posterior verificação:

- Espera-se que a maioria dos sistemas populares seja madura e sua criação tenha ocorrido, no mínimo, há 3 anos.
- Espera-se que repositórios populares recebam muitas contribuições externas, refletidas no número de pull requests aceitas.
- Espera-se que a maioria desses sistemas lance releases com regularidade mínima de 3 meses.
- Espera-se que os repositórios sejam atualizados com frequência mínima de 1 semana.
- Espera-se que prevaleçam linguagens como JavaScript, Python, e Java.
- Espera-se que a maioria dos sistemas populares possua um alto percentual de issues fechadas, de 75% ou mais.

## 3. Metodologia

 A coleta de dados foi realizada a partir da API do GitHub e implementada via GraphQL, buscando os 1.000 repositórios com maior número de estrelas. As seguintes métricas foram utilizadas para cada pergunta de pesquisa:

#### RQ-1: "Os sistemas populares são maduros/antigos?"
- `created_at_median`: valor mediano de dias desde a criação dos 1.000 principais repositórios GitHub

#### RQ-2: "Os sistemas populares recebem muita contribuição externa?"
- `merged_pull_requests_median`: valor mediano do número de pull requests incorporadas nos 1.000 principais repositórios do GitHub

#### RQ-3: "Os sistemas populares lançam releases com frequência?"
- `total_releases_mean`: valor médio do número de releases nos 1.000 principais repositórios do GitHub

#### RQ-4: "Os sistemas populares são atualizados com frequência?"
- `last_updated_median`: valor mediano de minutos desde a última atualização dos 1.000 principais repositórios do GitHub

#### RQ-5: "Os sistemas populares são escritos nas linguagens mais populares?"

- `main_language`: frequência das principais linguagens de programação usadas nos 1.000 principais repositórios do GitHub

#### RQ-6: "Os sistemas populares possuem um alto percentual de questões fechadas?"

1. `all_issues`: quantidade total de problemas dos 1.000 principais repositórios do GitHub
2. `closed_issues`: quantidade de problemas fechados dos 1.000 principais repositórios do GitHub
3. `closed_issues_ratio`: razão de questões fechadas, definido por:
  ```math
    closed\_issues\_ratio = \frac{closed\_issues}{all\_issues}
  ```

- `closed_issues_ratio_median`: mediana da razão de problemas fechados dos 1.000 principais repositórios do GitHub