import requests
from bs4 import BeautifulSoup
import os

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def checar_preco(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Busca o valor numérico do produto no Mercado Livre
        price_elem = soup.find('span', class_='andes-money-amount__fraction')
        if price_elem:
            preco = float(price_elem.text.replace('.', ''))
            return preco
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
    return None

def executar():
    watchlist = [
        {"nome": "Redmi Note 15 Pro 5G (512GB)", "url": "https://lista.mercadolivre.com.br/redmi-note-15-pro-512gb", "meta": 2500.00},
        {"nome": "Redmi Pad 2 (8GB RAM)", "url": "https://lista.mercadolivre.com.br/redmi-pad-2-8gb", "meta": 1500.00}
    ]

    for item in watchlist:
        preco = checar_preco(item["url"])
        if preco:
            print(f"[{item['nome']}] Preço atual: R$ {preco:.2f}")
            if preco <= item["meta"]:
                print(f"ALERT: {item['nome']} atingiu o preço desejado (R$ {preco:.2f})!")
        else:
            print(f"Não foi possível obter o preço para {item['nome']}")

if __name__ == "__main__":
    executar()