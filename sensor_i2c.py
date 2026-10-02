import random
import time

#direcciones I2C asignada al sensor de energia (ej. 0x40)
DIRECCION_I2C = "0X40"
print(f"--buscando dispositivos en direccion I2C: {DIRECCION_I2C} ---")

for lectura in range(1, 4):
    voltaje = round(random.uniform(118.0, 122.0), 1)
    corriente = round(random.uniform(1.0, 4.5), 2)
    potencia = round(voltaje * corriente, 1)

    print(
        f"[lectura {lectura}] Bus I2C -> {voltaje}V | {corriente}A | potencia:"
        f"{potencia}W"
    )
    time.sleep(1)