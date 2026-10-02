import pandas as pd

#bloque 1:limpieza de series de tiempo 

print("--- 1. CARGA Y FORMATEO DE DATOS ---")
# carga el csv generado en el monitoreo modbus 
df = pd.read_csv('lecturas_modbus.csv')

#convertir todos los nombres de la columnas a minusculas y quitar espacios 
df.columns = df.columns.str.lower().str.strip()

#buscar automaticamente la columna de tiempo (sirve 'timestamp', 'fecha')
col_tiempo = [c for c in df.columns if 'time' in c or 'fecha' in c][0]

# convertir de tiempo a datatime
df[col_tiempo] = pd.to_datetime(df[col_tiempo])

#poner el tiempo como indice principal
df.set_index(col_tiempo, inplace=True)

#verificar que no haya datos faltantes 
print("\nValores nulos por columna:")
print(df.isnull().sum())

#promediar los datos por cada 1 minuto ('1min')
df_minuto = df.resample('1min').mean().dropna()

print("\n---DATOS PROMEDIADOS POR MINUTO ---")
print(df_minuto.head())

#bloque 2: calculo de energia y potencia 
print("\n---2. CALCULO DE INDICADORES ENERGETICOS ---")

#intervalo de muestreo (modbus lee cada 3 segundos)
INTERVALO_SEGUNDOS = 3
HORAS_POR_MUESTRA = INTERVALO_SEGUNDOS / 3600.0

#1. CONSUMO DE ENERGIA ACUMULADO (kwh)
#energia (wh) = potencia (w) * tiempo (horas)
df['energia_wh'] = df['potencia_w'] * HORAS_POR_MUESTRA
consumo_total_kwh = df['energia_wh'].sum() / 1000.0 

#2. demanda maxima (kw)
demanda_maxima_kw = df['potencia_w'].max() / 1000.0

#3. potencia promedio (kw)
potencia_promedio_kw = df['potencia_w'].mean() / 1000.0

# 4. factor de carga (FC = potencia promedio / demanda maxima)
factor_de_carga = potencia_promedio_kw / demanda_maxima_kw if demanda_maxima_kw > 0 else 0

# desplegar los resultados 
print(f"- consumo total acumulado: {consumo_total_kwh:.4f} kWh")
print(f"- demanda maxima: {demanda_maxima_kw:.4f} kW")
print(f"- potencia promedio: {potencia_promedio_kw:.4f} kW")
print(f"- factor de carga (FC): {factor_de_carga:.4f} ({factor_de_carga * 100:.2f}%)")

#BLOQUE 3 VISUALIZACION CON MATPLOTLIB
import matplotlib.pyplot as plt

print("\n---3. GENERANDO GRAFICOS DE CONSUMO ---")

#configurar el estilo visual de la grafica 
plt.style.use('seaborn-v0_8-darkgrid' if 'seaborn-v0_8-darkgrid' in plt.style.available else 'default')

# GRAFICO 1:CURVA DE CARGA DIARIA Y DEMANDA MAXIMA 
fig, ax1 = plt.subplots(figsize=(10, 5))

#graficar la potencia instantanea en el tiempo 
ax1.plot(df.index, df['potencia_w'], color='tab:blue', label='Potencia Activa (W)', linewidth=1.5)
ax1.axhline(y=demanda_maxima_kw * 1000, color='tab:red', linestyle='--', label=f'Demanda Maxima ({demanda_maxima_kw:.2f} kW)')

ax1.set_title('Curva de Carga Energetica y Demanda Maxima', fontsize=14, fontweight='bold')
ax1.set_xlabel('Timestamp', fontsize=11)
ax1.set_ylabel('Potencia (W)', fontsize=11, color='tab:blue')
ax1.legend(loc='upper right')
ax1.grid(True, linestyle=':', alpha=0.6)

plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('grafico1_curva_carga.png', dpi=300)
print("- Grafico 1 guardado como 'grafico1_curva_carga.png'")
plt.close()

#Grafico 2: ocomparativa de voltaje vs corriente 
fig, ax2_vol = plt.subplots(figsize=(10,5))

color_vol = 'tab:green'
ax2_vol.set_xlabel('Timestamp', fontsize=11)
ax2_vol.set_ylabel('Voltaje (V)', color=color_vol, fontsize=11)
ax2_vol.plot(df.index, df['voltaje_v'], color=color_vol, label='Voltaje (V)', alpha=0.8)
ax2_vol.tick_params(axis='y', labelcolor=color_vol)

#crear segundo eje y para la corriente 
ax2_cor = ax2_vol.twinx()
color_cor = 'tab:orange'
ax2_cor.set_ylabel('Corriente (A)', color=color_cor, fontsize=11)
ax2_cor.plot(df.index, df['corriente_a'], color=color_cor, label='Corriente (A)', linestyle='--')
ax2_cor.tick_params(axis='y', labelcolor=color_cor)

plt.title('Comportamiento de voltaje vs Corriente', fontsize=14, fontweight='bold')
fig.tight_layout()
plt.savefig('grafico2_voltaje_vs_corriente.png', dpi=300)
print("- Grafico 2 guardado como 'grafico2_voltaje_vs_corriente.png'")
plt.close()
