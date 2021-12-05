from src.domain.seller import Seller


class SellersService:
    sellers = [
        Seller("Matheus"),
        Seller("Yullia"),
        Seller("Marcos"),
        Seller("Alessandra"),
        Seller("Anderson"),
    ]

    @classmethod
    def validate_seller(cls, seller_name):
        return seller_name in [seller.name for seller in cls.sellers]

    @classmethod
    def avaliable_sellers(cls):
        return [seller.name for seller in cls.sellers]
