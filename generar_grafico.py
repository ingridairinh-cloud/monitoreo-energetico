import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

NOMBRE_ARCHIVO = 'lecturas_modbus.csv'
UMBRAL_SOBREVOLTAJE = 135  # Límite en Volts

try:
    df = pd.read_csv(NOMBRE_ARCHIVO)
    print(" Carga de datos exitosa.")
except FileNotFoundError:
    print(f" No se encontró el archivo '{NOMBRE_ARCHIVO}'.")
    exit()

# Convertir el timestamp a formato datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# FILTRO: Tomar solo las lecturas de los últimos 30 minutos para evitar datos viejos
ultima_lectura = df['Timestamp'].max()
df = df[df['Timestamp'] >= (ultima_lectura - pd.Timedelta(minutes=30))]

# Configurar el lienzo de la gráfica
plt.figure(figsize=(12, 6))

# Trazar la curva principal de Voltaje
plt.plot(df['Timestamp'], df['Voltaje_V'], label='Voltaje Medido (V)', color='#1f77b4', linewidth=2, marker='o', markersize=4)

# Línea de umbral (135V)
plt.axhline(y=UMBRAL_SOBREVOLTAJE, color='red', linestyle='--', linewidth=2, label=f'Límite de Alerta ({UMBRAL_SOBREVOLTAJE}V)')

# Resaltar picos de sobrevoltaje
fallas = df[df['Voltaje_V'] > UMBRAL_SOBREVOLTAJE]

if not fallas.empty:
    plt.scatter(fallas['Timestamp'], fallas['Voltaje_V'], color='red', s=80, zorder=5, label='Pico de Sobrevoltaje')
    
    # Anotaciones sin amontonarse (solo muestra el valor si hay suficiente espacio)
    for i, (_, fila) in enumerate(fallas.iterrows()):
        # Alterna la posición del texto (arriba/abajo) para evitar empalmes
        offset_y = 12 if i % 2 == 0 else -18
        plt.annotate(f"{fila['Voltaje_V']}V", 
                     (fila['Timestamp'], fila['Voltaje_V']),
                     textcoords="offset points", 
                     xytext=(0, offset_y), 
                     ha='center', 
                     fontsize=9,
                     fontweight='bold', 
                     color='darkred')

# Formato del eje X (Hora:Minuto:Segundo)
gca = plt.gca()
gca.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

# Títulos y etiquetas
plt.title('Monitoreo de Voltaje en Tiempo Real - Calidad de Energía (Modbus TCP)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Tiempo (Hora:Minuto:Segundo)', fontsize=11, labelpad=10)
plt.ylabel('Voltaje (V)', fontsize=11, labelpad=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', frameon=True)
plt.xticks(rotation=30)
plt.tight_layout()

# Guardar la gráfica mejorada
NOMBRE_GRAFICA = 'grafica_calidad_energia.png'
plt.savefig(NOMBRE_GRAFICA, dpi=300)
print(f" Chart mejorado guardado como '{NOMBRE_GRAFICA}'.")

plt.show()