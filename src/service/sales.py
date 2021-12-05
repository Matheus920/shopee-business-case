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
