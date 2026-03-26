import pandas as pd
import streamlit as st

from app.services.analytics import calculate_kpis, load_sample_data

st.set_page_config(page_title="AI PoC Governance Hub", layout="wide")
st.title("AI PoC Governance Hub")
st.caption("Dashboard portfolio: ocena i monitoring inicjatyw AI / Big Data")

try:
    df = load_sample_data()
except FileNotFoundError:
    df = pd.DataFrame()

kpis = calculate_kpis(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Liczba PoC", kpis["total_pocs"])
col2.metric("Średni wynik", kpis["avg_score"])
col3.metric("Rekomendacje GO", kpis["go_count"])
col4.metric("Wysokie ryzyko", kpis["high_risk_count"])

st.subheader("Portfel inicjatyw")
st.dataframe(df, use_container_width=True)

if not df.empty:
    st.subheader("Top inicjatywy")
    top_df = df.sort_values(by="final_score", ascending=False)[
        ["title", "business_unit", "final_score", "recommendation"]
    ].head(5)
    st.dataframe(top_df, use_container_width=True)

    st.subheader("Inicjatywy wymagające guardrails")
    guardrails = df[df["recommendation"].isin(["GO_WITH_GUARDRAILS", "REVIEW"])]
    st.dataframe(guardrails, use_container_width=True)
else:
    st.info("Brak danych demo. Dodaj plik CSV lub uruchom API i rozbuduj dashboard.")
