# Notebook — Regressão Linear Múltipla (target: `SCORE_CREDITO`)

Modelo de Credit Scoring da Quantum Finance usando a base
`../data/Base_ScoreCredito_QuantumFinance(10).csv`.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `modelo_credit_scoring.ipynb` | Notebook completo, já executado (com gráficos e resultados) |
| `requirements.txt` | Dependências |

Ao executar o notebook, são gerados nesta pasta `modelo_score.json`, com os
coeficientes do modelo final, e `simulador_score_credito.xlsx`, no qual o
analista informa os dados do cliente e obtém o score e a faixa de risco.

## Etapas do notebook

3. **Preparação dos dados** — ausentes, duplicados, outliers (IQR) e dummies de `sexo`, `estado_civil`, `escola` e `reg_moradia`
4. **Análise descritiva** — média, mediana, desvio padrão, mínimo e máximo; histogramas e boxplots; tabelas de frequência e boxplots do score por categoria
5. **Correlação** — heatmap, variáveis mais relacionadas ao score e pares com risco de multicolinearidade
6. **Regressão linear múltipla** — treino/teste 70/30, seleção *stepwise backward* por p-valor, equação e interpretação dos coeficientes
7. **Suposições** — QQ-plot e Shapiro-Wilk, resíduo × previsto e Breusch-Pagan, Durbin-Watson, VIF
8. **Qualidade do modelo** — R², R² ajustado, RMSE, MAE e MAPE na base de teste
9. **Árvore de decisão** — mesmas métricas, importância das variáveis e comparação com a regressão
10. **Simulador** — função Python, coeficientes em JSON e planilha Excel

## Principais resultados (base de teste)

| Modelo | R² | R² ajustado | RMSE | MAE | MAPE |
|---|---|---|---|---|---|
| Regressão linear (19 variáveis) | 0,627 | 0,625 | 81,7 | 62,1 | 14,2% |
| Árvore de decisão | 0,685 | 0,683 | 75,2 | 55,6 | 12,6% |

## Como executar

```bash
pip install -r requirements.txt
jupyter notebook modelo_credit_scoring.ipynb   # gera o JSON e o Excel
```

Execute o notebook a partir desta pasta ou abra-o pelo diretório raiz. O código
procura a base em `../data` e `data` para funcionar nos dois contextos.
