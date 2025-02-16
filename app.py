# Latest Quotes for Dow Jones and Nasdaq 100

import requests
from datetime import datetime

def fetch_latest_quotes():
    url_dow = "https://api.example.com/dowjones/latest"
    url_nasdaq = "https://api.example.com/nasdaq100/latest"
    
    response_dow = requests.get(url_dow)
    response_nasdaq = requests.get(url_nasdaq)
    
    if response_dow.status_code == 200 and response_nasdaq.status_code == 200:
        dow_data = response_dow.json()
        nasdaq_data = response_nasdaq.json()
        
        return dow_data, nasdaq_data
    else:
        return None, None

def print_quotes():
    dow, nasdaq = fetch_latest_quotes()
    
    if dow and nasdaq:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Date and Time: {current_time}")
        print(f"Dow Jones Latest Quote: {dow['quote']} (Time: {dow['time']})")
        print(f"Nasdaq 100 Latest Quote: {nasdaq['quote']} (Time: {nasdaq['time']})")
    else:
        print("Failed to fetch quotes.")

if __name__ == "__main__":
    print_quotes()
