import unittest

import schema

from case import main


class SalesTest(unittest.TestCase):
    def test_invalid_seller_name(self):
        with self.assertRaises(schema.SchemaError):
            main(
                [
                    "--seller",
                    "invalidSellerName",
                    "--date",
                    "2021-12-25",
                    "--value",
                    "20.2",
                    "--item",
                    "Test Item",
                    "--customer",
                    "Pedro",
                ]
            )
