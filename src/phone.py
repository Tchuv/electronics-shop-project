from src.item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if number_of_sim <1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.number_of_sim = number_of_sim



    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        return self.quantity + other.quantity
