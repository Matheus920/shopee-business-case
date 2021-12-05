"""Domain class defining what a sale is consisted of"""


class Sell:
    def __init__(self, seller, customer, date, item_name, value):
        self.seller = seller
        self.customer = customer
        self.date = date
        self.item_name = item_name
        self.value = value
