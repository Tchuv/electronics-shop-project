from src.keyboard import KeyBoard

def test_keyBoard():
    kb = KeyBoard('SPELL', 1300, 2)
    assert str(kb) == "SPELL"
    assert str(kb.language) == "EN"
def test_change_lang():
    kb = KeyBoard('Электроника', 13000, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"
