import requests
from html.parser import HTMLParser
import time  # Import time module to add delay

# Custom HTMLParser to extract the stock quote from the HTML content
class StockQuoteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.price = None

    def handle_starttag(self, tag, attrs):
        # Looking for the specific tag that contains the stock price
        if tag == 'fin-streamer':
            for attr, value in attrs:
                if attr == 'class' and 'Fw(b) Fz(36px) Mb(-4px) D(ib)' in value:
                    self.is_price_tag = True

    def handle_endtag(self, tag):
        if tag == 'fin-streamer':
            self.is_price_tag = False

    def handle_data(self, data):
        if self.is_price_tag:
            self.price = data.strip()

def fetch_stock_quote(url):
    try:
        # Send a GET request to fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Ensure we got a valid response

        # Parse the HTML content using the custom HTMLParser
        parser = StockQuoteParser()
        parser.feed(response.text)

        # Return the price found by the parser
        return parser.price
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
        
        # Add a delay between requests to avoid triggering rate limiting
        time.sleep(5)  # Delay of 5 seconds between each request

if __name__ == "__main__":
    get_stock_quotes()
