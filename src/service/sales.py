import json
import os.path
from pathlib import Path

from schema import And, Schema, Use

from src.service.sellers import SellersService
from src.utils.date_validation import date_validation


class SalesService:
    _schema = Schema(
        {
            "seller": And(
                SellersService.validate_seller,
                error=f"Seller name not found. "
                f"Avaliable sellers are: {SellersService.avaliable_sellers()}",
            ),
            "customer": And(Use(str), error="Customer name must be a string"),
            "date": And(date_validation, error="Date must be in yyyy-mm-dd format"),
            "value": And(Use(float), error="Sale value must be a float"),
            "item": And(Use(str), error="Item name must be a string"),
        }
    )

    @classmethod
    def validate_schema(cls, data):

        data = {k: v for k, v in data.items() if v is not None}

        return cls._schema.validate(data)

    @classmethod
    def insert_data(cls, data):
        path = Path(__file__).parent / "../data/sales.json"
        path = path.resolve()

        file_exists = os.path.exists(path)

        if file_exists:
            with open(path, "r+", encoding="utf-8") as current_file:
                current_json = json.load(current_file)
                current_json.append(data)
                current_file.truncate(0)
                current_file.seek(0)
                json.dump(current_json, current_file)
        else:
            with open(path, "w", encoding="utf-8") as current_file:
                new_json = [data]
                json.dump(new_json, current_file)
