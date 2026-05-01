import requests

def fetch_page(url):
    headers = {
        "User-Agent" : "Mozilla/5.0",
        "Accept-Language": "es-CO,es;q=0.9",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print("Error: ", response.status_code)
        return None