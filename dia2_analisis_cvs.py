#bloque 1:funciones para analaisis energetico
def calcular_energia_kwh(potencia_w, horas=1):
    """calcula el energia en kwh a partir de la potencia en watts."""
    return (potencia_w * horas) / 1000.0

def calcular_factor_potencia(potencia_w, voltaje_v, corriente_a):
    """calcula el factor de potencia (FP = P / (V * I))."""
    potencia_aparente = voltaje_v * corriente_a
    if potencia_aparente == 0:
        return 0.0
    fp = potencia_w / potencia_aparente
    return min(fp, 1.0) #el FP maximo ideal es 1.0

# --- pruebas del bloque 1 ---
lectura_potencia = 1450.0 #watts
lectura_voltaje = 121.0 #volts
lectura_corriente = 12.5 #amperes

energia = calcular_energia_kwh(lectura_potencia)
fp = calcular_factor_potencia(lectura_potencia, lectura_voltaje, lectura_corriente)

print("===PRUEBA BLOQUE 1. FUNCIONES ===")
print(f"energia consumida: {energia} kwh")
print(f"factor de potencia : {fp:.2f}")

# --- BLOQUE 2: Lectura de archivos CVS ---
print("\n=== PRUEBA BLOQUE 2: LECTURA DE CVS ===")

#abrir y leer el archivo renglon por renglon 
with open('datos_energia.csv', 'r') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())

# --- BLOQUE 3: Manejo de exceociones ---
print("\n=== PRUEBA BLOQUE 3: LECTURA CON TRY/EXCEPT ===")

try:
    with open('datos_energia.csv', 'r') as archivo:
        lineas = archivo.readlines()
        print("¡archivo leido existosamente!")
        for linea in lineas[1:]: #[1:]omitela linea de encabezado
            datos = linea.strip().split(',')
            lectura, voltaje, corrirnte, potencia = datos
            print((f"lectura {lectura}:{potencia} w a {voltaje} v"))

except FileNotFoundError:
    print("Error: el archivo 'datos_energia.csv' no existe en esta carpeta.")
except Exception as e:
    print(f"Ocurrio un error inesperado: {e}")

#--- BLOQUE 4: Lectura con pandas ---
import pandas as pd

print("\n=== PRUEBA BLOQUE 4: PANDAS ===")

#1. leerel archivo CSV
df = pd.read_csv('datos_energia.csv')

#2. eliminar espaciosen blanco alrededor de los nombres de columnas
df.columns = df.columns.str.strip()

#3. mostrar la tabla completa y el resumen estadistico
print(df)
print("\n--- RESUMEN ESTADISTICO ---")
print(df.describe())

#4. calcular la energia en kwh y la suma total
df['energia_kwh'] = df['potencia_W'] / 1000
energia_total = df['energia_kwh'].sum()

print(f"\nEnergia total consumida: {energia_total:.2f} kwh")
# ---calculos adicionales del ejercicio practico---
#1. factor de potencia (FP) promedio aproximado
#supuesto de carga inductiva tipica en monitoreo
df['factor_potencia'] = 0.95
fp_promedio = df['factor_potencia'].mean()

#2. deteccion de valores fuera de rango 
alertas_voltaje = df[(df['voltaje_V'] < 110) | (df['voltaje_V'] > 130)]

print(f"Factor de potencia promedio: {fp_promedio:.2f}")
print(f"lecturas fuera de rango detectadas: {len(alertas_voltaje)}")
if not alertas_voltaje.empty:
    print(alertas_voltaje)
#--- bloque 5: graficar datos matplotlib ---
import matplotlib.pyplot as plt

# crear grafica de barras para la potencia
plt.bar(df['lectura'], df['potencia_W'], color='orange')

#personalizar el grafico
plt.title('potencia por lectura (W)')
plt.xlabel('lectura')
plt.ylabel('potencia (W)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

#guardar la grafica como imagen PNG
plt.savefig("grafica_perfil_energito.png")
#mostrar la grafica
plt.show()
#guardar el CSV con las nuevas columnas calculadas
df.to_csv("datos_energia_procesados.csv", index=False)