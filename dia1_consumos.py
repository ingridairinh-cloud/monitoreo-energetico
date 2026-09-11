import matplotlib.pyplot as plt

#1. listas de consumos diarios (kwh)
consumos_diarios = [12.5, 8.3, 15.8, 4.2, 9.1, 14.0, 6.5]
dias = ["dia 1", "dia 2", "dia 3", "dia 4", "dia 5", "dia 6", "dia 7"]
#umbrales para clasificar
umbral_ALTO=10.0
umbral_BAJO=5.0

#2. calculos generales 
total= sum(consumos_diarios)
promedio=total/len(consumos_diarios)
maximo=max(consumos_diarios)

print("=== REPORTE DE CONSUMO ENERGETICO ===")
print("consumo total:", total, "kwh")
print("promedio diario:", promedio, "kwh")
print("consumo maximo:", maximo, "kwh")
print("\n--- clasificacion diaria ---")

#3. bucle para clasificar cada dia 
dia=1
for consumo in consumos_diarios:
    if consumo > umbral_ALTO:
     categoria = "alto"
    elif consumo >= umbral_BAJO:
     categoria = "normal"
    else:
     categoria = "bajo"
    print("dia", dia, ":", consumo, "kwh -> categoria:", categoria)
    dia = dia +1
#4. generar la grafica para el reporte 
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 4))
plt.bar(dias, consumos_diarios, color='skyblue')
plt.axhline(y=umbral_ALTO, color='red', linestyle='--', label='umbral alto (10 kwh)')
plt.axhline(y=umbral_BAJO, color='green', linestyle='--', label='umbral bajo (5 kwh)')

plt.title('consumo diario de energia (kwh)')
plt.xlabel('dias')
plt.ylabel('kwh')
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.7)

#mostrar la grafica 
plt.show()