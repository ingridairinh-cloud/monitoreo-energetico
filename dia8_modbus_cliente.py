import time
import csv
from datetime import datetime
from pymodbus.client import ModbusTcpClient

# 1. Configuración de conexión al servidor simulado
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5020
CSV_FILE = 'lecturas_modbus.csv'
INTERVALO_SEGUNDOS = 3

def iniciar_cliente():
    # Crear el cliente Modbus TCP
    client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)

    # Intentar conectar
    if not client.connect():
        print("No se pudo conectar al servidor Modbus. ¿Está corriendo el servidor?")
        return

    print(f"Conectado exitosamente al servidor Modbus TCP ({SERVER_IP}:{SERVER_PORT})")
    print(f"Guardando lecturas en '{CSV_FILE}' cada {INTERVALO_SEGUNDOS} segundos...")
    print("Presiona Ctrl + C en esta terminal para detener la lectura.\n")

    # Crea la cabecera del archivo CSV si no existe 
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Voltaje_V', 'Corriente_A', 'Potencia_W', 'Frecuencia_Hz'])
    except FileExistsError:
        pass  # El archivo ya existía, no sobrescribimos el encabezado

    try:
        while True:
            # Leemos 4 registros a partir de la dirección 1 usando el parámetro esclavo correcto
            # Cambia address=1 por address=0
            respuesta = client.read_holding_registers(address=0, count=4, slave=1)


            if not respuesta.isError():
                datos = respuesta.registers
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # CORRECCIÓN DE SINTAXIS: Asignación correcta de índices del arreglo
                voltaje = datos[0]
                corriente = datos[1]
                potencia = datos[2]
                frecuencia = datos[3]

                print(f"[{timestamp}] Cliente -> Voltaje: {voltaje}V | Corriente: {corriente}A | Potencia: {potencia}W | Freq: {frecuencia}Hz")

                # Guardar en archivo CSV 
                with open(CSV_FILE, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([timestamp, voltaje, corriente, potencia, frecuencia])
            else:
                print(" Error al leer los registros Modbus. Intentando de nuevo...")

            time.sleep(INTERVALO_SEGUNDOS)

    except KeyboardInterrupt:
        print("\n Lectura detenida por el usuario. Cerrando cliente Modbus...")
    finally:
        client.close()

if __name__ == "__main__":
    iniciar_cliente()
