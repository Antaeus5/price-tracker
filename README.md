# Price Tracker Web Scraper

A Python-based web scraping tool that extracts product data (title, price, and link) from e-commerce websites and stores it in a structured CSV format.

---

## Features

* Extracts product titles, prices, and URLs
* Saves data into CSV files
* Clean and modular code structure
* Easy to adapt to different websites

---

## Technologies Used

* Python
* requests
* BeautifulSoup
* pandas

---

## Project Structure

```
price-tracker/
│
├── src/              # Core logic (scraper, parser, storage)
├── data/             # Output files (ignored in Git)
├── config/           # Future configurations
│
├── main.py           # Entry point
├── requirements.txt
└── README.md
```

---

## How to Run

1. Clone the repository:

```
git clone https://github.com/Antaeus5/price-tracker.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the scraper:

```
python main.py
```

---

## Example Output

| Title          | Price  | Link                |
| -------------- | ------ | ------------------- |
| Sample Product | £50.00 | https://example.com |

---

## Use Cases

* Price monitoring
* Competitor analysis
* Data collection for e-commerce
* Market research

---

##  Future Improvements

* Price change tracking
* Multi-page scraping
* Scheduled execution
* API integration

---

## 👤 Author

Antaeus5
