"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_pos():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.price == 10000
    assert item1.name == "Смартфон"


def test_calculate_total_price():
    item2 = Item("Ноутбук", 20000, 5)
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item3 = Item("Телевизор", 20000, 1)
    Item.pay_rate = 0.5
    item3.apply_discount()
    assert item3.pay_rate == 0.5
    assert item3.price == 10000


# def test_name():
#     item.name = 'Смартфон'
#     assert Item.name == 'Смартфон'
#     # Item.name = 'СуперСмартфон'
#     # assert Item.name == 'Смартфон'



def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'
