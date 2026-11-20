from discount_strategy import DiscountStrategy


class BulkDiscount(DiscountStrategy):

    def __init__(self, threshold: float, amount: float) -> None:
        self.__threshold: float = threshold  # minimum total to qualify
        self.__amount: float = amount        # amount taken off

    def apply(self, total: float) -> float:
        if total >= self.__threshold:
            return total - self.__amount
        return total