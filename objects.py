#This file will contain object structures

class Creature(Object):
    _health = "100"
    _mana = "100"
	_dmg = "100"
	_absorb = "100"

    pass

class Herro(Creature, Bag):
    _stamina = "100"


    def minus_stamina(self, value):
        self._stamina -= value



    def refill_stamina(self, value):
            self._stamina += value

    pass

class Bag(Object):
    _articles_off = []
    _articles_on = []

    def wear_item(self, item_index):
       __value = self._articles_off[item_index].pop
        self._articles_on.append(__value)


    def strip_item(self, item_index):
        __value = self._articles_on[item_index].pop
        self.articles_off.append(__value)

    pass


class Item(Object):
    def __init__(self, health = 0, mana = 0, dmg = 0, absorb = 0, stamina = 0, attack = 0, defence = 0):
        self._health = health
        self._mana = mana
        self._dmg = dmg
        self._absorb = absorb
        self._stamina = stamina
        self._attack = attack
        self._defence = defence

    pass