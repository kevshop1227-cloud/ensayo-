import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🚜 Dashboard Cosecha - KPIs Maquinaria")

# 🔹 Filtros simulados
col1, col2, col3 = st.columns(3)

with col1:
    frente = st.selectbox("Frente", ["Todos", "Frente 1", "Frente 2"])

with col2:
    maquina = st.selectbox("Máquina", ["Todas", "M01", "M02"])

with col3:
    operador = st.selectbox("Operador", ["Todos", "Juan", "Pedro"])

# 🔹 KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Horas Productivas", "8.5 h", "0.5")
col2.metric("Disponibilidad", "92%", "2%")
col3.metric("Eficiencia", "87%", "-3%")
col4.metric("Motor Encendido", "10.2 h", "⚠️")

# 🔹 Alertas
st.subheader("⚠️ Alertas")
st.warning("Máquina M01 con baja eficiencia")
st.error("Motor encendido alto sin producción")

# 🔹 Tabla
st.subheader("📊 Detalle")

data = pd.DataFrame({
    "Fecha": ["2026-04-20", "2026-04-20"],
    "Máquina": ["M01", "M02"],
    "Operador": ["Juan", "Pedro"],
    "Horas": [8.5, 7.2],
    "Estado": ["Productivo", "Parada"]
})

st.dataframe(data, use_container_width=True)