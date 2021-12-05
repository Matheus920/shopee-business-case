import csv
import os.path
from pathlib import Path

from src.domain.seller import Seller


class SellersService:
    _sellers = [
        Seller("Matheus"),
        Seller("Yullia"),
        Seller("Marcos"),
        Seller("Alessandra"),
        Seller("Anderson"),
    ]

    _csv_path = (Path(__file__).parent / "../data/rank.csv").resolve()

    @classmethod
    def validate_seller(cls, seller_name):
        return seller_name in [seller.name for seller in cls._sellers]

    @classmethod
    def avaliable_sellers(cls):
        return [seller.name for seller in cls._sellers]

    @classmethod
    def build_csv(cls):
        if not os.path.exists(cls._csv_path):
            with open(cls._csv_path, "w", encoding="utf-8", newline="") as rank_csv:
                csv_writer = csv.DictWriter(
                    rank_csv, fieldnames=["seller", "value"], delimiter=","
                )
                for seller in cls._sellers:
                    csv_writer.writerow({"seller": seller.name, "value": 0})
