from src.phone import Phone
from src.item import Item
def test_pos():
    phone2 = Phone("Samsung", 10000, 3, 2)
    assert phone2.price == 10000
    assert phone2.name == "Samsung"
    assert phone2.number_of_sim == 2

def test_vid():
    phone1 = Phone("Nokia", 5000, 10, 1)
    assert str(phone1) == 'Nokia'
    assert repr(phone1) == "Phone('Nokia', 5000, 10, 1)"
    assert phone1.number_of_sim == 1

def test_add():
    phone1 = Phone("Nokia", 5000, 10, 1)
    item1 = Item("LG", 10000, 20)
    assert item1 + phone1 == 30
    assert phone1 + phone1 == 20