import abc


class BaseProduct(abc.ABC):
    """Your code goes here! :D """

    def __init__(self, price: float, quantitity: int, name: str) -> None:
        self.name = name
        self.price = price
        self.quantity = quantitity

    def __repr__(self):
        return self.name
