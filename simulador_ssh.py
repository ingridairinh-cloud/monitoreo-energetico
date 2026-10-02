import time 
import getpass

print("="*50)
print("SIMULADOR DE CONEXION SSH - RASPBERRY PI")
print("="*50)

host = input("ssh ")
if "@" in host: 
    usuario, ip = host.split("@")
else:
    usuario = "pi"
    ip = host

print(f"\n[OpenSSH] conectando a{ip} en el puerto 22...")
time.sleep(1.5)
print(f"[OpenSSH] Host {ip} encontrado. estableciendo tunel cifrado TLA/SSH...")
time.sleep(1)

password = getpass.getpass(prompt=f"{usuario}@{ip}'s password: ")
print("\nautenticando...")
time.sleep(1)
print("="*50)
print("lunux raspberrypi 6.1.21-v8+ #1642 SMP PREEMPT")
print("debian GNU/Lunix 11 (bullseye)")
print("="*50)
print(f"Bienbenido a Raspberry Pi OS. Sesion remota activa para '{usuario}'.\n")

while True:
    comando = input(f"{usuario}@raspberrypi:~ $ ")
    if comando.strip() == "exit":
        print("\nCerrando sesion SSH y liberando puerto 22... ¡conexion terminada!")
        break
    elif comando.strip() == "uname -a":
        print("linux raspberrypi 6.1.21-v8+ #1642 SMP PREEMPT aarch64 GNU/linux")
    elif comando.strip() == "ifconfig" or comando.strip() == "ip a":
        print("wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500")
        print(f"       inet {ip}  netmask 255.255.255.0  broadcast 192.168.1.255")
    elif comando.strip() == "hostname -I":
        print(f"{ip}")
    elif comando.strip() == "":
        continue
    else: 
        print(f"bash: {comando}: orden no encontrada (simulado)")