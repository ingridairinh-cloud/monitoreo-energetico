import subprocess
import time
from pyngrok import ngrok

#1. configurar el token de ngrok
ngrok.set_auth_token("3KNQoTvSH2v7sDP5OrHeArIK4AU_7k4CGNKEdhWbJua6zsjZ4")

#2. iniciar el servidor de streamlit en segundo plano
print("⚡Iniciando el servidor de Streamlit...")
proceso_sreamlit = subprocess.Popen(["Streamlit", "run", "dia10_dashboard.py"])

#esperamos 5 segundos para streamlit alcance a encender
time.sleep(5)

#3. abrir el tunel de ngrok al puerto 8501
print("Abriendo el tunel publico con Ngrok...")
public_url = ngrok.connect(8501)

print("\n" + "=" *60)
print(f"🚀 ¡SISTEMA LISTO! tu dashboard esta en vivo en:")
print(f"-> {public_url}")
print("=" * 60 + "\n")

#4. mantener ambos procesos abiertos hasta que presiones Ctrl + c 
try:
    proceso_sreamlit.wait()
except KeyboardInterrupt:
    print("\n 🔴 Apagado el servidor y cerrado el tunel...")
    ngrok.kill()
    proceso_sreamlit.terminate()
    print("🟢 Sistema apagado correctamente.")
