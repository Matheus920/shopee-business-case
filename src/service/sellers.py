import csv
import os.path
from pathlib import Path

from src.domain.seller import Seller

"""Static class for actions between the sellers and other modules"""


class SellersService:
    _sellers = [
        Seller("Matheus"),
        Seller("Yullia"),
        Seller("Marcos"),
        Seller("Alessandra"),
        Seller("Anderson"),
    ]

    _csv_path = (Path(__file__).parent / "../data/rank.csv").resolve()

    """Utility function created to verify if the provided seller name is valid or not"""

    @classmethod
    def validate_seller(cls, seller_name: str) -> bool:
        return seller_name in [seller.name for seller in cls._sellers]

    """Function that returns all avaliable sellers
    defined as constant by the requirements"""

    @classmethod
    def avaliable_sellers(cls) -> list:
        return [seller.name for seller in cls._sellers]

    """If the csv ranking doesnt exist yet,
    we create for each seller a row containing 0 as their cumulated sales"""

    @classmethod
    def build_csv(cls) -> None:
        if not os.path.exists(cls._csv_path):
            with open(cls._csv_path, "w", encoding="utf-8", newline="") as rank_csv:
                csv_writer = csv.DictWriter(
                    rank_csv, fieldnames=["seller", "value"], delimiter=","
                )
                for seller in cls._sellers:
                    csv_writer.writerow({"seller": seller.name, "value": 0})
