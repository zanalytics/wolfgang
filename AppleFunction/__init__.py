import logging
from typing import Dict
import yfinance as yf
import pandas as pd
from typing import Dict
from utils.stock_market import stock_market

def main(name: str) -> Dict[str, int]:
    apple = stock_market(name)
    json_apple = apple.to_json(orient='records')
    return json_apple