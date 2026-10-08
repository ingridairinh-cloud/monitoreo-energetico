from pyngrok import ngrok
ngrok.set_auth_token("3KNQoTvSH2v7sDP5OrHeArIK4AU_7k4CGNKEdhWbJua6zsjZ4")
#abre el tunel al puerto de streamlit
public_url = ngrok.connect(8501)
print("\n=" *10)
print(f"🚀 Tu Dashboard publico esta en: {public_url}")
print("=\n" * 10)
input()