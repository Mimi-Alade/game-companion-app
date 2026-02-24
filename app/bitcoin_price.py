import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin")
        response.raise_for_status()
        return response.json()["quotes"]["USD"]["price"]

    except requests.exceptions.RequestException as e:
        print("Error fetching Bitcoin price:", e)
        return None

def main():
    price = get_bitcoin_price()
    print(f"Current Bitcoin price: ${price:.2f}")

if __name__ == "__main__":
    main()

