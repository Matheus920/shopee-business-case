from src.domain.seller import Seller


class SellersService:
    def __init__(self):
        self.sellers = [
            Seller("Matheus"),
            Seller("Yullia"),
            Seller("Marcos"),
            Seller("Alessandra"),
            Seller("Anderson"),
        ]

    def validate_seller(self, seller_name):
        return seller_name in [seller.name for seller in self.sellers]

    def avaliable_sellers(self):
        return [seller.name for seller in self.sellers]
