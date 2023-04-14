import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        calculate_total_price = self.price * self.quantity
        return calculate_total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name:str):
        if len(name) >10:
            raise Exception('Длина товара превышает 10 символов.')
        self.__name = name

    # @classmethod
    # def instantiate_from_csv(cls, CSV_PATH='../src/items.csv'):
    #     with open(CSV_PATH) as file:
    #         file_reader = csv.DictReader(file, delimiter=',')
    #         for i in file_reader:
    #             name, price, quantity = i.get('name'), int(i.get('price')), int(i.get('quantity'))
    #             cls.all.append((name, price, quantity))

    @staticmethod
    def string_to_number(number: str) -> int:
        """Cтатический метод, возвращающий число из числа-строки
        :return: Число в нужном нам формате
        """
        return int(number.split(".")[0])

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other:'Item'):
        if isinstance(other, Item) or isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError('нельзя было сложить `Phone` или `Item` с экземплярами не `Phone` или `Item`')

    @classmethod
    def instantiate_from_csv(cls, CSV_PATH='../src/items.csv') -> None:
        try:
            with open(CSV_PATH) as file:
                file_reader = csv.DictReader(file, delimiter=',')
                for i in file_reader:
                    if any(i.get(value) is None for value in ['name', 'price', 'quantity']):
                        raise exceptions.exceptions.InstantiateCSVError
                    name, price, quantity = i.get('name'), int(i.get('price')), int(i.get('quantity'))
                    cls.all.append((name, price, quantity))

        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        except csv.Error:
            print('Файл item.csv поврежден')

