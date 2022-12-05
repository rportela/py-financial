import pandas as pd
from datetime import date
from zipfile import ZipFile
from .CachedSession import CachedSession


class BinanceHistoricalData:
    def __init__(self) -> None:
        self.url_base = "https://data.binance.vision/data"
        self.session = CachedSession()

    def _zipurl_to_df(self, url: str) -> pd.DataFrame:
        """Unzips a cached version of an url to a data frame.

        Args:
            url (str): _description_

        Returns:
            pd.DataFrame: _description_
        """
        dfs = []
        with self.session.get(f"{self.url_base}{url}") as res:
            with ZipFile(res) as zip:
                for name in zip.namelist():
                    with zip.open(name) as entry:
                        df = pd.read_csv(entry, sep=",")
                        dfs.append(df)
        return pd.concat(dfs)

    def get_futures_um_daily_klines(
        self, ticker: str, interval: str, dt: date
    ) -> pd.DataFrame:
        """Gets binance futures UM daily klines

        Args:
            ticker (str): _description_
            interval (str): _description_
            dt (date): _description_

        Returns:
            pd.DataFrame: _description_
        """
        ticker = ticker.upper()
        file_name = f"{ticker}-{interval}-{dt.strftime('%Y-%m-%d')}.zip"
        url = f"/futures/um/daily/klines/{ticker}/{interval}/{file_name}"
        return self._zipurl_to_df(url)

    def get_futures_um_monthly_klines(
        self, ticker: str, interval: str, year: int, month: int
    ) -> pd.DataFrame:
        """Gets binance futures UM monthly klines

        Args:
            ticker (str): _description_
            interval (str): _description_
            year (int): _description_
            month (int): _description_

        Returns:
            pd.DataFrame: _description_
        """
        ticker = ticker.upper()
        file_name = f"{ticker}-{interval}-{year}-{str(month).zfill(2)}.zip"
        url = f"/futures/um/monthly/klines/{ticker}/{interval}/{file_name}"
        return self._zipurl_to_df(url)
