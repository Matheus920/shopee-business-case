import csv
import json
import os.path
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

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
        tempfile = NamedTemporaryFile(mode="w", delete=False)
        file_exists = os.path.exists(path)

        if file_exists:
            with open(path, "r", encoding="utf-8") as current_file, tempfile:
                current_json = json.load(current_file)
                current_json.append(data)
                json.dump(current_json, tempfile)
            shutil.move(tempfile.name, path)
        else:
            with open(path, "w", encoding="utf-8") as current_file:
                new_json = [data]
                json.dump(new_json, current_file)

        csv_path = Path(__file__).parent / "../data/rank.csv"
        csv_path = csv_path.resolve()
        tempfile = NamedTemporaryFile(mode="w", delete=False)

        if file_exists:
            with open(
                csv_path, "r", encoding="utf-8", newline=""
            ) as rank_file, tempfile:
                csv_reader = csv.DictReader(
                    rank_file, delimiter=",", fieldnames=["seller", "value"]
                )
                csv_writer = csv.DictWriter(
                    tempfile, delimiter=",", fieldnames=["seller", "value"]
                )
                for row in csv_reader:
                    if row["seller"] == data["seller"]:
                        row["value"] = float(row["value"]) + data["value"]
                    csv_writer.writerow(row)
            shutil.move(tempfile.name, csv_path)
        else:
            with open(csv_path, "w", encoding="utf-8", newline="") as rank_file:
                csv_writer = csv.DictWriter(
                    rank_file, delimiter=",", fieldnames=["seller", "value"]
                )
                csv_writer.writerow({"seller": data["seller"], "value": data["value"]})
