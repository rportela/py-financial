from datetime import datetime


class Candle:
    """
    The representation of a candle
    """
    def __init__(
        self,
        ticker: str,
        open_time: datetime,
        close_time: datetime,
        open: float,
        high: float,
        low: float,
        close: float,
        volume: float,
        quantity: float,
    ) -> None:
        self.ticker = ticker
        self.open_time = open_time
        self.close_time = close_time
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.quantity = quantity
