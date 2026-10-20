"""Simulador de SCORE_CREDITO — Quantum Finance.

Usa a equação da regressão linear múltipla salva pelo notebook em `modelo_score.json`.
Execução: streamlit run app_simulador.py
"""
import json
from pathlib import Path

import streamlit as st

MODELO = json.loads((Path(__file__).parent / "modelo_score.json").read_text(encoding="utf-8"))
COEFS = MODELO["coeficientes"]
CATEGORIAS = MODELO["categorias"]


def calcular_score(cliente):
    """Intercepto + soma(coeficiente x valor). Categóricas viram dummies (1 se for a categoria)."""
    contribuicoes = {"intercepto": MODELO["intercepto"]}
    for termo, coef in COEFS.items():
        if termo in cliente:
            valor = float(cliente[termo])
        else:
            var, cat = next((v, termo[len(v) + 1:]) for v in CATEGORIAS if termo.startswith(v + "_"))
            valor = 1.0 if str(cliente[var]) == cat else 0.0
        contribuicoes[termo] = coef * valor
    return sum(contribuicoes.values()), contribuicoes


def faixa_risco(score):
    for faixa in MODELO["faixas_risco"]:
        if faixa["minimo"] is None or score >= faixa["minimo"]:
            return faixa["faixa"]


st.set_page_config(page_title="Simulador de Score — Quantum Finance", page_icon="💳")
st.title("Simulador de Score de Crédito")
st.caption("Quantum Finance — modelo de regressão linear múltipla (target: SCORE_CREDITO)")

col1, col2 = st.columns(2)
with col1:
    idade = st.number_input("Idade (anos)", 18, 100, 40)
    sexo = st.selectbox("Sexo", CATEGORIAS["sexo"])
    estado_civil = st.selectbox("Estado civil", CATEGORIAS["estado_civil"])
    escola = st.selectbox("Escolaridade", CATEGORIAS["escola"])
    reg_moradia = st.selectbox("Região de moradia", CATEGORIAS["reg_moradia"])
    qte_dependentes = st.number_input("Quantidade de dependentes", 0, 10, 1)
with col2:
    trabalha = st.checkbox("Trabalha", value=True)
    vl_salario_mil = st.number_input("Salário (R$ mil)", 0.0, 500.0, 60.0, disabled=not trabalha)
    tempo_ultimoservico = st.number_input("Tempo no último serviço", 0, 60, 30)
    casa_propria = st.checkbox("Possui casa própria", value=False)
    vl_imovel_em_mil = st.number_input("Valor do imóvel (R$ mil)", 0.0, 5000.0, 0.0, disabled=not casa_propria)
    qte_cartoes = st.number_input("Quantidade de cartões", 0, 10, 1)
    qte_carros = st.number_input("Quantidade de carros", 0, 10, 1)

cliente = {
    "idade": idade, "sexo": sexo, "estado_civil": estado_civil, "escola": escola, "reg_moradia": reg_moradia,
    "Qte_dependentes": qte_dependentes, "tempo_ultimoservico": tempo_ultimoservico, "trabalha": int(trabalha),
    "vl_salario_mil": vl_salario_mil if trabalha else 0.0, "casa_propria": int(casa_propria),
    "vl_imovel_em_mil": vl_imovel_em_mil if casa_propria else 0.0,
    "Qte_cartoes": qte_cartoes, "Qte_carros": qte_carros,
}
score, contribuicoes = calcular_score(cliente)

st.divider()
c1, c2 = st.columns(2)
c1.metric("Score previsto", f"{score:,.1f}")
c2.metric("Faixa de risco", faixa_risco(score))
st.caption(f"Erro médio do modelo na base de teste: MAE ≈ {MODELO['metricas_teste']['MAE']:.0f} pontos.")

with st.expander("Como o score foi calculado"):
    st.table({"termo": list(contribuicoes), "pontos": [round(v, 2) for v in contribuicoes.values()]})
