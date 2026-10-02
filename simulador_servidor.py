import asyncio
import random
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusServerContext, ModbusSlaveContext

# 1. Creamos el bloque de datos que inicia en la dirección 1
block = ModbusSequentialDataBlock(1, [120, 5, 600, 60])
store = ModbusSlaveContext(hr=block)

# Configuramos explícitamente el Slave ID 1 para que tu cliente lo encuentre al conectarse
context = ModbusServerContext(slaves={1: store}, single=False)

async def actualizar_mediciones(data_block):
    print("Simulación iniciada. Generando datos con picos de sobrevoltaje...\n")
    
    while True:
        es_falla = random.random() < 0.20
        
        if es_falla:
            voltaje = random.randint(138, 155)
            corriente = random.randint(12, 18)
            print("¡ALERTA! Pico de sobrevoltaje/sobrecorriente generado.")
        else:
            voltaje = random.randint(118, 122)
            corriente = random.randint(4, 6)
            
        potencia = voltaje * corriente
        frecuencia = random.choice([59, 60, 60, 60, 61])
        
        valores_nuevos = [voltaje, corriente, potencia, frecuencia]
        
        # CORRECCIÓN DEFINITIVA: Usamos setValues con "V" mayúscula
        data_block.setValues(1, valores_nuevos)
        
        print(f"Servidor -> Voltaje: {voltaje}V | Corriente: {corriente}A | Potencia: {potencia}W | Freq: {frecuencia}Hz")
        await asyncio.sleep(3)

async def run_server():
    # Iniciamos la tarea de simulación pasando el bloque de datos
    asyncio.create_task(actualizar_mediciones(block))
    print("Servidor Modbus TCP activo en 127.0.0.1:5020...")
    await StartAsyncTcpServer(context=context, address=("127.0.0.1", 5020))

if __name__ == "__main__":
    asyncio.run(run_server())
