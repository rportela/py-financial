import unittest
from src.py_financial.services import BinanceHistoricalData
from datetime import date


class TestBinanceHistoricalData(unittest.TestCase):

    def test_futures_daily_btcusdt_15m(self):
        service = BinanceHistoricalData()
        df = service.get_futures_um_daily_klines("BTCUSDT", "15m", date(2022, 12, 2))
        self.assertIsNotNone(df)
        self.assertTrue(len(df) > 10)

    def test_futures_monthly_btcusdt_15m(self):
        service = BinanceHistoricalData()
        df = service.get_futures_um_monthly_klines("BTCUSDT", "15m", 2022, 10)
        self.assertIsNotNone(df)
        self.assertTrue(len(df) > 10)