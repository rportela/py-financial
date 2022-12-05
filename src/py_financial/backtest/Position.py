from datetime import datetime
from typing import Union


class Position:
    def __init__(
        self,
        ticker: str,
        open_price: float,
        open_time: Union[datetime, None] = None,
        short: bool = False,
    ) -> None:
        self.ticker = ticker
        self.open_price = open_price
        self.open_time = open_time if open_time else datetime.now()
        self.short = short
