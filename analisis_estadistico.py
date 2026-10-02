import pandas as pd

NOMBRE_ARCHIVO = 'lecturas_modbus.csv'
UMBRAL_SOBREVOLTAJE = 135

try:
    df = pd.read_csv(NOMBRE_ARCHIVO)
    
    total_lecturas = len(df)
    fallas = df[df['Voltaje_V'] > UMBRAL_SOBREVOLTAJE]
    total_fallas = len(fallas)
    porcentaje_fallas = (total_fallas / total_lecturas) * 100 if total_lecturas > 0 else 0
    
    v_max = df['Voltaje_V'].max()
    v_min = df['Voltaje_V'].min()
    v_prom = df['Voltaje_V'].mean()
    p_prom = df['Potencia_W'].mean()

    print("=" * 60)
    print("      RESUMEN ESTADÍSTICO DE CALIDAD DE ENERGÍA   ")
    print("=" *60)
    print(f"• Total de registros analizados: {total_lecturas}")
    print(f"• Total de picos de sobrevoltaje (>135V): {total_fallas}")
    print(f"• Porcentaje de eventos anómalos: {porcentaje_fallas:.2f}%")
    print("-"*50)
    print(f"• Voltaje Máximo Registrado: {v_max} V")
    print(f"• Voltaje Mínimo Registrado: {v_min} V")
    print(f"• Voltaje Promedio: {v_prom:.2f} V")
    print(f"• Potencia Promedio Consumida: {p_prom:.2f} W")
    print("=" *60)

except FileNotFoundError:
    print(f"No se encontró el archivo '{NOMBRE_ARCHIVO}'.")