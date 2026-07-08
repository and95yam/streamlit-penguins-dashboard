import streamlit as st
import plotly.express as px
import pandas as pd

from src.data_utils import (
    validar_extension_csv,
    cargar_csv,
    obtener_columnas_numericas,
    obtener_columnas_categoricas,
    filtrar_registros,
)


# ============================================================
# Configuración general de Streamlit
# ============================================================

st.set_page_config(
    page_title="Analizador Profesional de Datos",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# Estilos visuales personalizados
# ============================================================

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #1F4E79;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #555555;
    }
    .info-box {
        background-color: #F0F6FC;
        padding: 18px;
        border-radius: 12px;
        border-left: 6px solid #1F77B4;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# Encabezado principal
# ============================================================

st.markdown('<p class="main-title">📊 Analizador Profesional de Datos</p>',
unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Carga un archivo CSV y genera visualizaciones automáticas para análisis exploratorio.</p>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# Carga del archivo CSV
# ============================================================

st.sidebar.header("📁 Carga de archivo")

archivo = st.sidebar.file_uploader(
    "Seleccione un archivo CSV",
    type=["csv"]
)

if archivo is None:
    st.info("Por favor, cargue un archivo con extensión `.csv` para iniciar el análisis.")
    st.stop()

if not validar_extension_csv(archivo.name):
    st.error("Formato inválido. Solo se permiten archivos con extensión `.csv`.")
    st.stop()

try:
    df = cargar_csv(archivo)

except ValueError as error:
    st.error(str(error))
    st.stop()


# ============================================================
# Validaciones generales del DataFrame
# ============================================================

if df.empty:
    st.error("El archivo cargado no contiene datos.")
    st.stop()

if df.shape[1] < 2:
    st.error("El archivo debe contener al menos dos columnas para realizar el análisis.")
    st.stop()

st.success("Archivo CSV cargado correctamente.")


# ============================================================
# Resumen del archivo
# ============================================================

st.markdown(
    f"""
    <div class="info-box">
        <b>Resumen del archivo:</b><br>
        Filas: {df.shape[0]}<br>
        Columnas: {df.shape[1]}
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# Optimización para gráficas
# ============================================================

MAX_REGISTROS_GRAFICA = 1000

if len(df) > MAX_REGISTROS_GRAFICA:
    st.info(
        f"El archivo contiene {len(df)} registros. "
        f"Para optimizar la visualización se usará una muestra aleatoria de "
        f"{MAX_REGISTROS_GRAFICA} registros en algunas gráficas."
    )

    df_grafica = df.sample(MAX_REGISTROS_GRAFICA, random_state=42)

else:
    df_grafica = df.copy()


# ============================================================
# Identificación de columnas
# ============================================================

columnas_numericas = obtener_columnas_numericas(df)
columnas_categoricas = obtener_columnas_categoricas(df)

if len(columnas_numericas) == 0:
    st.warning("El archivo no contiene columnas numéricas suficientes para generar gráficos.")
    st.stop()


# ============================================================
# Visualizaciones
# ============================================================

st.header("📈 Visualizaciones de análisis de datos")

col1, col2 = st.columns(2)


# ============================================================
# Gráfico de barras
# ============================================================

with col1:
    st.subheader("📊 Gráfico de barras")

    if columnas_categoricas:
        columna_categoria = st.selectbox(
            "Seleccione una columna categórica",
            columnas_categoricas,
            key="bar_categoria"
        )

        columna_valor = st.selectbox(
            "Seleccione una columna numérica",
            columnas_numericas,
            key="bar_valor"
        )

        try:
            datos_barra = (
                df.groupby(columna_categoria, as_index=False)[columna_valor]
                .sum()
                .sort_values(by=columna_valor, ascending=False)
            )

            fig_bar = px.bar(
                datos_barra,
                x=columna_categoria,
                y=columna_valor,
                title=f"Suma de {columna_valor} por {columna_categoria}"
            )

            st.plotly_chart(fig_bar, use_container_width=True)

        except Exception as error:
            st.error(f"No se pudo generar el gráfico de barras: {error}")

    else:
        st.warning("No existen columnas categóricas para generar el gráfico de barras.")


# ============================================================
# Gráfico de líneas
# ============================================================

with col2:
    st.subheader("📈 Gráfico de líneas")

    columna_linea = st.selectbox(
        "Seleccione columna numérica para el gráfico de líneas",
        columnas_numericas,
        key="line_valor"
    )

    try:
        if "Order Date" in df.columns:
            df_linea = df.copy()

            df_linea["Order Date"] = pd.to_datetime(
                df_linea["Order Date"],
                errors="coerce"
            )

            df_linea = df_linea.dropna(subset=["Order Date"])

            datos_linea = (
                df_linea
                .groupby(pd.Grouper(key="Order Date", freq="ME"))[columna_linea]
                .sum()
                .reset_index()
            )

            fig_line = px.line(
                datos_linea,
                x="Order Date",
                y=columna_linea,
                title=f"Evolución mensual de {columna_linea}"
            )

        else:
            fig_line = px.line(
                df_grafica,
                y=columna_linea,
                title=f"Evolución de {columna_linea}"
            )

        st.plotly_chart(fig_line, use_container_width=True)

    except Exception as error:
        st.error(f"No se pudo generar el gráfico de líneas: {error}")


# ============================================================
# Gráfico de dispersión
# ============================================================

st.subheader("🔎 Gráfico de dispersión")

if len(columnas_numericas) >= 2:
    eje_x = st.selectbox(
        "Seleccione eje X",
        columnas_numericas,
        key="scatter_x"
    )

    eje_y = st.selectbox(
        "Seleccione eje Y",
        columnas_numericas,
        key="scatter_y"
    )

    try:
        fig_scatter = px.scatter(
            df_grafica,
            x=eje_x,
            y=eje_y,
            title=f"Relación entre {eje_x} y {eje_y}",
            render_mode="svg"
        )

        st.plotly_chart(fig_scatter, use_container_width=True)

    except Exception as error:
        st.error(f"No se pudo generar el gráfico de dispersión: {error}")

else:
    st.warning("Se requieren al menos dos columnas numéricas para el gráfico de dispersión.")
