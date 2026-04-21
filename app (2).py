import streamlit as st
import pandas as pd

# 🔧 Configuración
st.set_page_config(page_title="Dashboard Cosecha", layout="wide")

# 🎨 Estilos personalizados
st.markdown("""
<style>
.metric-card {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    text-align: center;
}
.metric-title {
    font-size: 16px;
    color: #555;
}
.metric-value {
    font-size: 28px;
    font-weight: bold;
}
.green {color: #2ecc71;}
.orange {color: #f39c12;}
.red {color: #e74c3c;}
</style>
""", unsafe_allow_html=True)

# 📌 Sidebar
st.sidebar.title("🚜 Agro Dashboard")
menu = st.sidebar.radio("Menú", ["Dashboard", "Reportes", "Configuración"])

# 📌 Header
st.title("Dashboard de Cosecha")
st.caption("Monitoreo de KPIs de maquinaria")

# 📌 Filtros
col1, col2, col3, col4 = st.columns(4)

frente = col1.selectbox("Frente", ["Todos", "Frente 1", "Frente 2"])
maquina = col2.selectbox("Máquina", ["Todas", "M01", "M02"])
operador = col3.selectbox("Operador", ["Todos", "Juan", "Pedro"])
fecha = col4.date_input("Fecha")

# 📊 KPIs
st.subheader("Indicadores")

col1, col2, col3, col4 = st.columns(4)

col1.markdown("""
<div class="metric-card">
<div class="metric-title">Horas Productivas</div>
<div class="metric-value green">8.5 h</div>
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div class="metric-card">
<div class="metric-title">Disponibilidad</div>
<div class="metric-value green">92%</div>
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div class="metric-card">
<div class="metric-title">Eficiencia</div>
<div class="metric-value orange">87%</div>
</div>
""", unsafe_allow_html=True)

col4.markdown("""
<div class="metric-card">
<div class="metric-title">Motor Encendido</div>
<div class="metric-value red">10.2 h</div>
</div>
""", unsafe_allow_html=True)

# 🚨 Alertas
st.subheader("Alertas")

st.error("Motor encendido alto sin producción (M02)")
st.warning("Eficiencia baja en máquina M01")

# 📋 Tabla
st.subheader("Detalle de Operación")

data = pd.DataFrame({
    "Fecha": ["2026-04-20", "2026-04-20"],
    "Frente": ["Frente 1", "Frente 2"],
    "Máquina": ["M01", "M02"],
    "Operador": ["Juan", "Pedro"],
    "Estado": ["Productivo", "Parada"],
    "Horas": [8.5, 7.2]
})

st.dataframe(data, use_container_width=True)
