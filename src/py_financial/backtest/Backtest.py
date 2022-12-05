from datetime import datetime
from typing import List, Union, Dict
from .Position import Position
import pandas as pd


class Backtest:
    def __init__(self, capital: float) -> None:
        self.capital = capital
        self.positions: Dict[str, List[Position]]

    def total_profit(self) -> float:
        profit = 0.0
        for pos in self.positions.values():
            for p in pos:
                if not p.is_open:
                    profit += p.profit
        return profit

    def total_profit_pct(self) -> float:
        profit = 1.0
        for pos in self.positions.values():
            for p in pos:
                if not p.is_open:
                    profit *= 1 + p.profit_pct
        return profit - 1.0

    def get_last(self, ticker: str) -> Union[Position, None]:
        vlist = self.positions.get(ticker)
        return vlist[-1] if vlist else None

    def is_last_open(self, ticker: str) -> bool:
        last = self.get_last(ticker)
        return last.is_open if last else False

    def open(self, ticker: str, price: float, short: bool = False) -> Position:
        last = self.get_last(ticker)
        if last and last.short == short:
            return last
        else:
            if last and last.is_open:
                last.close(price)
            last = Position(ticker, price, datetime.now(), short)
            plist = self.positions.get(ticker)
            if not plist:
                plist = []
                self.positions[ticker] = plist
            plist.append(last)
            return last

    def close(self, ticker: str, price: float) -> Union[Position, None]:
        last = self.get_last(ticker)
        if last:
            last.close(price)
        return last

    def positions_df(self) -> pd.DataFrame:
        lst = []
        for pos in self.positions.values():
            lst += pos
        return pd.DataFrame(lst)

    def act(
        self, ticker: str, price: float, signal: float, tolerance: float
    ) -> Union[Position, None]:
        if signal >= tolerance:
            return self.open(ticker, price, True)
        elif signal <= -tolerance:
            return self.open(ticker, price, False)
        else:
            return None
