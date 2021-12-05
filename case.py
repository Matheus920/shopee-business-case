import argparse


def register_sell():
    raise NotImplementedError


parser = argparse.ArgumentParser(description="register a sell for a specific seller")

parser.add_argument("--seller", help="Seller name")
parser.add_argument("--customer", help="Customer name")
parser.add_argument("--date", help="dd-MM-yyyy date which sell has been made")
parser.add_argument("--item", help="Item name")
parser.add_argument("--value", help="Sell value")

result = parser.parse_args()

print(result)
