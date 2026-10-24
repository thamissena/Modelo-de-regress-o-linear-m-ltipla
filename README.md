# Quantum Finance — Credit Scoring

Projeto de Applied Statistics para estimar o `SCORE_CREDITO` de clientes da
Quantum Finance por meio de regressão linear múltipla e árvore de decisão.

## Estrutura

- `data/Base_ScoreCredito_QuantumFinance(10).csv`: base com 10.127 clientes.
- `notebook/modelo_credit_scoring.ipynb`: análise completa,
  treinamento, diagnóstico, comparação dos modelos e simulador em Python.
- `notebook/requirements.txt`: dependências do projeto.

O notebook também gera, na pasta `notebook/`, os arquivos
`modelo_score.json` (coeficientes da regressão final) e
`simulador_score_credito.xlsx` (simulador em Excel). Esses arquivos são
artefatos gerados, não são necessários para executar a análise do zero.

## Análises realizadas

- preparação dos dados, tratamento das categorias e criação de variáveis dummy;
- análise descritiva e correlações;
- regressão linear múltipla com seleção *stepwise backward*;
- diagnóstico de normalidade, homocedasticidade, independência,
  multicolinearidade e pontos influentes;
- árvore de decisão com validação cruzada e comparação por R², RMSE, MAE e MAPE;
- simulação de score pela equação final e exportação para Excel.

## Como executar

```bash
cd notebook
pip install -r requirements.txt
jupyter notebook modelo_credit_scoring.ipynb
```

Execute as células do notebook a partir da pasta `notebook/`. O código localiza
a base tanto em `../data` quanto em `data`, e salva os artefatos gerados na
pasta de execução.
