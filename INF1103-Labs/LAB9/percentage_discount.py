from discount_strategy import DiscountStrategy


class PercentageDiscount(DiscountStrategy):

    def __init__(self, percent: float) -> None:
        if percent < 0 or percent > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.__percent: float = percent  # e.g. 10 means 10% off

    def apply(self, total: float) -> float:
        return total * (1 - self.__percent / 100)