from datetime import datetime


class Position:
    def __init__(
        self, ticker: str, open_time: datetime, open_price: float, short: bool = False
    ) -> None:
        self.ticker = ticker
        self.open_time = open_time
        self.open_price = open_price
        self.short = short
