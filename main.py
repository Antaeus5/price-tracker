from src.scraper import fetch_page
from src.parser import parse_products
from src.storage import save_to_csv


URL = "https://books.toscrape.com/"

def main():
    print("Fetching page...")
    html = fetch_page(URL)

    if html:
        products = parse_products(html)
        save_to_csv(products, "data/products.csv")

        print(f"Scraped {len(products)} products")
    else:
        print("no HTML received")

if __name__ == "__main__":
    print("Starting program...")
    main()