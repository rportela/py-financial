from datetime import datetime
from typing import Union


class Position:
    def __init__(
        self,
        ticker: str,
        open_price: float,
        open_time: Union[datetime, None] = None,
        short: bool = False,
        is_open: bool = True,
    ) -> None:
        self.ticker = ticker
        self.open_price = open_price
        self.open_time = open_time if open_time else datetime.now()
        self.short = short
        self.is_open = is_open

    def close(self, close_price: float):
        self.is_open = False
        self.close_price = close_price
        self.profit = (
            self.close_price - self.open_price
            if not self.short
            else self.open_price - self.close_price
        )
        self.profit_pct = self.profit / self.open_price
