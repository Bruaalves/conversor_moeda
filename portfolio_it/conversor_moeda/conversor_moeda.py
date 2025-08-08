import requests

def converter(valor, moeda):
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    resposta = requests.get(url).json()
    taxa = resposta['rates'].get(moeda)
    if taxa is None:
        raise ValueError("Moeda inválida.")
    return valor * taxa

while True:
    try:
        valor = float(input("Valor em BRL: "))
        moeda = input("Converter para qual moeda? (ex: USD, EUR): ").upper()
        convertido = converter(valor, moeda)
        print(f"Valor em {moeda}: {convertido:.2f}")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    continuar = input("Deseja converter outro valor? (s/n): ").strip().lower()
    if continuar != 's':
        print("FIM.")
        break

