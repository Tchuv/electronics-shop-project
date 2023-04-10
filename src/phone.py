from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if new_number_of_sim > 0:
            self.__number_of_sim = new_number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __add__(self, other: 'Item'):
        if isinstance(other, Item) or isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError('нельзя сложить `Phone` или `Item` с экземплярами не `Phone` или `Item`')


