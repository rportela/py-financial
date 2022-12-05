import requests
import os
from io import BufferedReader


class CachedSession:
    def __init__(self) -> None:
        self.session = requests.Session()

    def get(self, url: str) -> BufferedReader:
        dbar = url.find("//")
        cache_name = os.path.join("/tmp", *url[dbar + 2:].split("/"))
        if not os.path.exists(cache_name):
            lbar = url.rfind("/")
            file_path = url[dbar + 2:lbar]
            cache_folder = os.path.join("/tmp", *file_path.split("/"))
            os.makedirs(cache_folder, exist_ok=True)
            with self.session.get(url) as res:
                with open(cache_name, "wb") as dest:
                    dest.write(res.content)
        return open(cache_name, "rb")
