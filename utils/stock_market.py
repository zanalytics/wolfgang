import yfinance as yf


def stock_market(company: str):
    data = yf.download(tickers=company, period='7d', interval='1h')
    data['Company'] = company
    return data

if __name__ == "__main__":
    google_data = stock_market("GOOG")
    print(f"The shape of the data is {google_data.shape}")
    print(google_data.head())