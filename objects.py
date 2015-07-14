#This file will contain object structures
class Creature(object):
    def minus_health(self, health):
        self._health -= health

    def refill_health(self, health):
        self._health += health

    def __init__(self, health = 0, mana = 0, dmg = 0, absorb = 0):
        self._health = health
        self._mana = mana
        self._dmg = dmg
        self._absorb = absorb


class Bag(object):
    _articles_off = []
    _articles_on = []

    def wear_item(self, item_index):
        __value = self._articles_off.pop(item_index)
        self._articles_on.append(__value)

    def strip_item(self, item_index):
        __value = self._articles_on.pop(item_index)
        self.articles_off.append(__value)


class Hero(Creature, Bag):
    def minus_stamina(self, value):
        self._stamina -= value

    def refill_stamina(self, value):
            self._stamina += value

    def __init__(self, health = 0, mana = 0, dmg = 0, absorb = 0, stamina = 0):
        Creature.__init__(self, health, mana, dmg, absorb)
        self._stamina = stamina


class Item(object):
    def __init__(self, health = 0, mana = 0, dmg = 0, absorb = 0, stamina = 0, attack = 0, defence = 0):
        self._health = health
        self._mana = mana
        self._dmg = dmg
        self._absorb = absorb
        self._stamina = stamina
        self._attack = attack
        self._defence = defence