import os
import shutil
import unittest

import schema

from case import main


class SalesTest(unittest.TestCase):
    def setUp(self) -> None:
        shutil.rmtree("./src/data")
        os.makedirs("./src/data")

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

    def test_invalid_date_format(self):
        with self.assertRaises(schema.SchemaError):
            main(
                [
                    "--seller",
                    "Yullia",
                    "--date",
                    "20-12-25",
                    "--value",
                    "20.2",
                    "--item",
                    "Test Item",
                    "--customer",
                    "Pedro",
                ]
            )

    def test_invalid_value_type(self):
        with self.assertRaises(schema.SchemaError):
            main(
                [
                    "--seller",
                    "Yullia",
                    "--date",
                    "2012-12-25",
                    "--value",
                    "a",
                    "--item",
                    "Test Item",
                    "--customer",
                    "Pedro",
                ]
            )

    def test_data_being_inserted(self):
        self.assertEqual(os.path.exists("./src/data/sales.json"), False)
        main(
            [
                "--seller",
                "Yullia",
                "--date",
                "2012-12-25",
                "--value",
                "10",
                "--item",
                "Test Item",
                "--customer",
                "Pedro",
            ]
        )
        self.assertEqual(os.path.exists("./src/data/sales.json"), True)

    def tearDown(self) -> None:
        shutil.rmtree("./src/data")
        os.makedirs("./src/data")
