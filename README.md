This is a simple Python-based script that fetches the current stock quotes for **Dow Jones** and **NASDAQ** from Yahoo Finance using web scraping. The script parses the HTML of the Yahoo Finance pages to extract the current stock prices. This project uses Python's built-in libraries to fetch and parse the data.

## Features
- Fetches the current stock prices for **Dow Jones** and **NASDAQ**.
- Parses Yahoo Finance pages to extract the stock quotes.
- No external dependencies required—uses only built-in Python libraries (`requests`, `html.parser`).
- Includes a delay between requests to avoid rate limiting from Yahoo Finance.

## Requirements
- Python 3.x (No need to install additional libraries like `BeautifulSoup` or `requests`—only built-in libraries are used)

## How to Run

### 1. Clone the Repository or Download the Script
You can clone the repository or download the Python script (`stock_quote_fetcher.py`).

### 2. Run the Script
Once the script is saved locally, open your terminal and navigate to the directory containing the script. Then, run the script with:

```
python stock_quote_fetcher.py
```

### 3. View the Output
The script will display the current stock prices for **Dow Jones** and **NASDAQ** in the terminal. If the data is fetched successfully, the output will look like this:

```
Dow Jones Current Price: 34,500.50
NASDAQ Current Price: 14,100.20
```

If there is an issue with fetching the data, the script will display an error message, such as:

```
Error fetching data: 429 Client Error: Too Many Requests for url: https://finance.yahoo.com/quote/%5EDJI
Could not retrieve Dow Jones price.
```

## How It Works
1. **Fetching Data**: The script sends HTTP `GET` requests to the Yahoo Finance pages for **Dow Jones** and **NASDAQ**.
2. **HTML Parsing**: It parses the HTML content of the pages using Python’s built-in `HTMLParser` to find and extract the stock prices.
3. **Display Output**: The current stock prices are displayed on the terminal.

## Rate Limiting
To avoid hitting rate limits from Yahoo Finance, the script includes a 5-second delay between requests. If you encounter the "429 Client Error: Too Many Requests" error, it may indicate that the script has made too many requests in a short time. You can either wait or adjust the delay as needed.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contributing
Feel free to fork the repository, create issues, and submit pull requests. Contributions are welcome!

## Acknowledgments
- This script uses **Yahoo Finance** for retrieving stock data. Visit [Yahoo Finance](https://finance.yahoo.com/) for more information.
