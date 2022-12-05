from typing import List
from .Position import Position

class Backtest:

    def __init__(self, capital: float) -> None:
        self.capital = capital
        self.positions: List[Position] = []
    