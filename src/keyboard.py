from src.item import Item


class MixinKeyboardLayout:
    def __init__(self, *args, **kwargs):
        self.__language = 'EN'
        super().__init__(*args, **kwargs)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'


class KeyBoard(MixinKeyboardLayout, Item):
    def __repr__(self) -> str:
        return super().__repr__().replace('Item', 'KeyBoard')