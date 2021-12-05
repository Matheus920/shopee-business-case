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
    _csv_path = (Path(__file__).parent / "../data/rank.csv").resolve()
    _sales_path = (Path(__file__).parent / "../data/sales.json").resolve()
    _ordered_ranking = list()

    @classmethod
    def validate_schema(cls, data):

        data = {k: v for k, v in data.items() if v is not None}

        return cls._schema.validate(data)

    @classmethod
    def insert_data(cls, data):
        tempfile = NamedTemporaryFile(mode="w", delete=False)
        file_exists = os.path.exists(cls._sales_path)

        if file_exists:
            with open(cls._sales_path, "r", encoding="utf-8") as current_file, tempfile:
                current_json = json.load(current_file)
                current_json.append(data)
                json.dump(current_json, tempfile)
            shutil.move(tempfile.name, cls._sales_path)
        else:
            with open(cls._sales_path, "w", encoding="utf-8") as current_file:
                new_json = [data]
                json.dump(new_json, current_file)

        tempfile = NamedTemporaryFile(mode="w", delete=False)

        with open(
            cls._csv_path, "r", encoding="utf-8", newline=""
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
        shutil.move(tempfile.name, cls._csv_path)

    @classmethod
    def print_sale_list(cls):
        with open(cls._csv_path, "r", encoding="utf-8") as rank_csv:
            csv_reader = csv.DictReader(rank_csv, fieldnames=["seller", "value"])
            for row in csv_reader:
                index = 0
                for rank in cls._ordered_ranking:
                    if rank[1] > row["value"]:
                        index = index + 1
                        continue
                cls._ordered_ranking.insert(index, tuple([row["seller"], row["value"]]))

        with open(cls._sales_path, "r", encoding="utf-8") as sales_list:
            sales_list = json.load(sales_list)

        for seller in cls._ordered_ranking:
            for sale in sales_list:
                if seller[0] == sale["seller"]:
                    print(json.dumps(sale))
