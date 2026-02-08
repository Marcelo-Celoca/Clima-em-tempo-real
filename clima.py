import requests

def consultar_clima():
    url_simples = "https://api.hgbrasil.com/weather?woeid=455827"

    print("--- Consultor de Clima Real ---")

    try:
        resposta = requests.get(url_simples)

        dados = resposta.json()

        cidade = dados['results']['city']
        temp = dados['results']['temp']
        descricao = dados['results']['description']
        humidade = dados['results']['humidity']

        print(f"\nCidade: {cidade}")
        print(f"Temperatura: {temp}ºC")
        print(f"Condição: {descricao}")
        print(f"Umidade: {humidade}%")

    except Exception as e:
        print(f"\033[31mX\033[m Erro ao conectar com a internet {e}")

if __name__ == "__main__":
    consultar_clima()
    