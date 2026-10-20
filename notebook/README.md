# Notebook — Regressão Linear Múltipla (target: `SCORE_CREDITO`)

Modelo de Credit Scoring da Quantum Finance usando a base `../data/Base_ScoreCredito_QuantumFinance*.csv`.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `modelo_regressao_linear_multipla_score.ipynb` | Notebook completo, já executado (com gráficos e resultados) |
| `simulador_score_credito.xlsx` | Simulador em Excel: o analista digita os dados do cliente e a planilha calcula o score e a faixa de risco |
| `app_simulador.py` | Simulador web em Streamlit |
| `modelo_score.json` | Coeficientes do modelo final (usados pelo app) |
| `requirements.txt` | Dependências |

## Etapas do notebook

3. **Preparação dos dados** — ausentes, duplicados, outliers (IQR) e dummies de `sexo`, `estado_civil`, `escola` e `reg_moradia`
4. **Análise descritiva** — média, mediana, desvio padrão, mínimo e máximo; histogramas e boxplots; tabelas de frequência e boxplots do score por categoria
5. **Correlação** — heatmap, variáveis mais relacionadas ao score e pares com risco de multicolinearidade
6. **Regressão linear múltipla** — treino/teste 70/30, seleção *stepwise backward* por p-valor, equação e interpretação dos coeficientes
7. **Suposições** — QQ-plot e Shapiro-Wilk, resíduo × previsto e Breusch-Pagan, Durbin-Watson, VIF
8. **Qualidade do modelo** — R², R² ajustado, RMSE, MAE e MAPE na base de teste
9. **Árvore de decisão** — mesmas métricas, importância das variáveis e comparação com a regressão
10. **Simulador** — função Python, planilha Excel e app Streamlit

## Principais resultados (base de teste)

| Modelo | R² | R² ajustado | RMSE | MAE | MAPE |
|---|---|---|---|---|---|
| Regressão linear (19 variáveis) | 0,627 | 0,625 | 81,7 | 62,1 | 14,2% |
| Árvore de decisão | 0,685 | 0,683 | 75,2 | 55,6 | 12,6% |

## Como executar

```bash
pip install -r requirements.txt
jupyter notebook modelo_regressao_linear_multipla_score.ipynb   # gera de novo o JSON e o Excel
streamlit run app_simulador.py                                  # abre o simulador no navegador
```
