import requests
from bs4 import BeautifulSoup

def fetch_stock_quote(url):
    try:
        # Send a GET request to fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Ensure we got a valid response
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the stock price (the price is within a span with a certain class name)
        price_tag = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
        
        if price_tag:
            return price_tag.text
        else:
            print(f"Error: Stock quote not found in the page.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def get_stock_quotes():
    # URLs for Dow Jones and NASDAQ
    stock_urls = {
        'Dow Jones': 'https://finance.yahoo.com/quote/^DJI',
        'NASDAQ': 'https://finance.yahoo.com/quote/^IXIC'
    }

    # Loop through the stock indices
    for index, url in stock_urls.items():
        price = fetch_stock_quote(url)
        if price:
            print(f"{index} Current Price: {price}")
        else:
            print(f"Could not retrieve {index} price.")

if __name__ == "__main__":
    get_stock_quotes()
