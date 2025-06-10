import requests

def get_price(crypto="dogecoin"):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data[crypto]["usd"]
    except:
        return None

def analyze_price(current_price):
    if current_price is None:
        return "Erro ao obter o preço."

    # Lógica exemplo (ajustável com indicadores no futuro)
    if current_price < 0.21:
        return f"COMPRA AGORA 🔥 | Preço: ${current_price:.4f} | Alvo: $0.225 🚀"
    elif current_price > 0.235:
        return f"VENDE JÁ 💸 | Preço: ${current_price:.4f} | Pode cair até $0.22 ⚠️"
    else:
        return f"Aguarda 📊 | Preço: ${current_price:.4f}"
