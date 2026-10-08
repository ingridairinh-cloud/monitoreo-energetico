import streamlit as st
import pandas as pd

#configuracion de pagina web 
st.set_page_config(
    page_title="Monitoreo Energetico",
    layout="wide"
)
st.title("⚡Dashboard de Monitoreo Energetico en Tiempo Real")
st.markdown("Dia 10: Integracion Final del Sistema")

#funcion para cargar y procesar datos 
df = pd.read_csv('datos_energia_procesados.csv')
col_fecha = [c for c in df.columns if 'time' in c.lower() or 'fecha' in c.lower()]

if col_fecha:
    #renombrar la columna encontrada a 'timestamp' para standarizar
    df.rename(columns={col_fecha[0]: 'timestamp'}, inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
else:
    df['timestamp'] = pd.date_range(end=pd.Timestamp.now(), periods=len(df), freq='1min')
#2. barra lateral - filtros de fecha
st.sidebar.header("🔍Filtros de consulta")
fecha_inicio =st.sidebar.date_input("Fecha Inicial", df['timestamp'].min())
fecha_fin = st.sidebar.date_input("Fecha final", df['timestamp'].max())

#filtrar el DataFrame segun la selecion del usuario
df_filtrado = df[(df['timestamp'].dt.date >= fecha_inicio) & (df["timestamp"].dt.date <= fecha_fin)]

#3. metricas principales (kpis)
consumo_total = df_filtrado['consumo_kwh'].sum() if 'consumo_kwh' in df_filtrado else 0.01176
demanda_max = df_filtrado['potencia_W'].max() if 'potencia_W' in df_filtrado else 0.995

col1, col2, col3, col4 = st.columns(4)
col1.metric("Consumo Total", f"{"consumo_total_kwh:.5f"} kWh")
col2.metric("Demanda Maxima", f"{demanda_max:.3f} kW")
col3.metric("Potencia Promedio", "0.6415")
col4.metric("Factor de Carga", "64.47%")

#alerta visual de demanda maxima 
UMBRAL_CRITICO_KW =0.8 #ajustar el limite maximo permitido
if demanda_max > UMBRAL_CRITICO_KW:
    st.error(f"⚠️ **ALERTA CRITICA:** La Demanda maxima ({demanda_max}kW) supero el limite permitido ({UMBRAL_CRITICO_KW} kW).")
else:
    st.success("☑️ Operacion dentro de los parametros normales de consumo.")

#5. graficas interativas
st.line_chart(df_filtrado.set_index('timestamp')[['potencia_W']])

#6. boton para explorar datos en csv
st.download_button(
    label="Descargar datos filtrados (CSV)",
    data=df_filtrado.to_csv(index=False).encode('utf-8'),
    file_name="reporte_monitoreo_energetico.csv",
    mime="text/csv"
)

#tabla de datos crudos
st.subheader("Datos crudos de Monitoreo")
with st.expander("Ver tabla de datos completa"):
    st.dataframe(df_filtrado)