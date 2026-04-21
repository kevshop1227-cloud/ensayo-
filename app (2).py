import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# 🎨 CSS avanzado
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.block-container {
    padding-top: 1rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f2a2a;
    color: white;
}

/* KPI cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.title {
    font-size: 14px;
    color: #888;
}

.value {
    font-size: 32px;
    font-weight: bold;
}

.green { color: #27ae60; }
.blue { color: #2980b9; }
.orange { color: #f39c12; }
.red { color: #e74c3c; }

/* Alerts */
.alert-box {
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 8px;
}
.alert-warning {
    background-color: #fff3cd;
}
.alert-danger {
    background-color: #f8d7da;
}
</style>
""", unsafe_allow_html=True)

# 🔷 Sidebar
st.sidebar.title("🌱 AGRO")
st.sidebar.markdown("---")
st.sidebar.write("📊 Dashboard")
st.sidebar.write("🚜 Maquinaria")
st.sidebar.write("👷 Operadores")
st.sidebar.write("⚙️ Configuración")

# 🔷 Header
st.title("Dashboard Cosecha")
st.caption("Monitoreo de KPIs de Maquinaria")

# 🔷 Filtros
col1, col2, col3, col4 = st.columns(4)

col1.selectbox("Frente", ["Todos", "Frente 1", "Frente 2"])
col2.selectbox("Máquina", ["Todas", "M01", "M02"])
col3.selectbox("Operador", ["Todos", "Juan", "Pedro"])
col4.date_input("Fecha")

# 🔷 KPIs
st.subheader("Indicadores")

c1, c2, c3, c4 = st.columns(4)

c1.markdown("""
<div class="card">
<div class="title">Horas Productivas</div>
<div class="value green">8.5 h</div>
</div>
""", unsafe_allow_html=True)

c2.markdown("""
<div class="card">
<div class="title">Disponibilidad</div>
<div class="value blue">92%</div>
</div>
""", unsafe_allow_html=True)

c3.markdown("""
<div class="card">
<div class="title">Eficiencia</div>
<div class="value orange">87%</div>
</div>
""", unsafe_allow_html=True)

c4.markdown("""
<div class="card">
<div class="title">Motor Encendido</div>
<div class="value red">10.2 h</div>
</div>
""", unsafe_allow_html=True)

# 🔷 Alertas
st.subheader("Alertas Activas")

st.markdown("""
<div class="alert-box alert-warning">
⚠️ Máquina M01 con baja eficiencia
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="alert-box alert-danger">
🔥 Motor encendido alto sin producción
</div>
""", unsafe_allow_html=True)

# 🔷 Tabla
st.subheader("Detalle de Eventos")

data = pd.DataFrame({
    "Fecha": ["2026-04-20", "2026-04-20"],
    "Frente": ["Frente 1", "Frente 2"],
    "Máquina": ["M01", "M02"],
    "Operador": ["Juan", "Pedro"],
    "Estado": ["Productivo", "Parada"],
    "Horas": [8.5, 7.2]
})

st.dataframe(data, use_container_width=True)
