"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_positiv():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.price == 10000
    assert item1.name == "Смартфон"

def test_calculate_total_price():
    item2 = Item("Ноутбук", 20000, 5)
    assert item2.calculate_total_price() == 100000
