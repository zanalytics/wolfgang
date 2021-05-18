import logging
from typing import Dict
import pandas as pd
from utils.stock_market import stock_market


def main(df: str) -> Dict[str, int]:
    data = pd.read_json(df)
    amazon = stock_market("AMZN")
    amazon_apple = pd.concat([amazon, data], ignore_index=False, sort=False)
    json_data = amazon_apple.to_json(orient='records')
    return json_data
