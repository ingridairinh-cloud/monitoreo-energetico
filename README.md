# monitoreo y procesamiento de datos energeticos 

proyecto de residensias para el monitoreo, analisis y visualiacion de datos de consumo energetico mediante python. 

---

## avance de proyecto

### dia 1: calculo de consumos electricios ('dia1_consumos.py')
* creacion de funciones para calcular energia consumida ($kWh$) y evaluar el factor de potencia.

### dia 2: analisis de datos en CSV ('dia2_analisis_cvs.py')
* procesamiento automatizado de mediciones energeticas desde el archivo 'datos _energia.csv'.
* exportacion de datos procesados ('datos_energia_procesados.csv').
* generacion de la grafica de perfil energetico:

![perfil energetico](grafica_perfil_energetico.png)

### dia 3: entorno de desarrollo y control de versiones 
* configuracion de VS Code y estructuracion del proyecto.
* gestion del repositorio Git local y remoto en GitHub ('monitoreo_energetico').

---

## archivos del repositorio
* 'dia1_comsumo.py': script para calculos electricos basicos.
* 'dia2_analisis_cvs.py': script para lectura, analisis y graficacion de datos.
* 'datos_energia.csv': datos de entrada.
* datos_energia_procesados.csv': datos calculados.
* 'grafica_perfil_energetico.png': grafica del perfil de consumo.

## resumen de matematicas clave 
| matematica energetica | valor obtenido |
| :--- | :--- |
| **lecturas procesadas** | registros de voltaje y corriente |
| **energia total consumida** | calculada en kwh |
| **fractor de promedio** | evaluando en el script |

## Dia 9: analisis y monitoreo energetico

en esta sesion se procesaron los datos del perfil de consumo y calidad de energia, calculando los siguientes indicadores clave:

- **Consumo total acumulado:** 0.1264 kwh
- **Demanda maxima:** 2.6640 kw
- **Potencia promedio:** 0.6744 kw
- **Factor de carga (FC):** 25.31%

### Graficas generales: 
1. **Curva de carga y demanda maxima ('grafico1_curva_carga.png'):** Muestra el pefil de potencia activa con la linea limites de demanda maxima.
2. **Voltaje vs Corriente ('grafico2_voltaje_vs_corriente.png'):** Comparativa del comportamiento electrico donde sse aprecia el incremento de corriente asociado al pico de potencia.