import argparse

from src.service.sales import SalesService
from src.service.sellers import SellersService

parser = argparse.ArgumentParser(description="Register a sale for a specific seller")

parser.add_argument("--seller", help="Seller name")
parser.add_argument("--customer", help="Customer name")
parser.add_argument("--date", help="yyyy-mmd-dd date which sale has been made")
parser.add_argument("--item", help="Item name")
parser.add_argument("--value", help="Sale value")

result = vars(parser.parse_args())

SellersService.build_csv()

validated_result = SalesService.validate_schema(result)

SalesService.insert_data(validated_result)

SalesService.print_sale_list()
