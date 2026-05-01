from bs4 import BeautifulSoup

def parse_products(html):
    soup = BeautifulSoup(html, "html.parser")
    products = []

    base_url = "https://books.toscrape.com/"

    items = soup.select("article.product_pod")

    print("Items encontrados:", len(items))

    for item in items:
        title = item.select_one("h3 a")["title"]
        price = item.select_one(".price_color").get_text()
        link = base_url + item.select_one("h3 a")["href"]

        products.append({
            "title": title,
            "price": price,
            "link": link
        })

    return products