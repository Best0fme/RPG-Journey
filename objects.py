#This file will contain object structures
class Creature(object):
    exp = 0

    def __init__(self, health=0, mana=0, dmg=0, absorb=0, lvl=0):
        self._health = health
        self._mana = mana
        self._dmg = dmg
        self._absorb = absorb
        self._lvl = lvl

    def refill_health(self, health):
        self._health += health

    def minus_health(self, health):
        self._health -= health

    def lvl_up(self):
        self._lvl += 1


class Bag(object):
    _articles_off = []
    _articles_on = []

    def wear_item(self, item_index, hero):
        if item_index._lvl <= hero._lvl:
            __value = self._articles_off.pop(item_index)
            self._articles_on.append(__value)
        else:
            pass

    def strip_item(self, item_index):
        __value = self._articles_on.pop(item_index)
        self.articles_off.append(__value)


class Hero(Creature, Bag):
    def __init__(self, health=0, mana=0, dmg=0, absorb=0, stamina=0, lvl=0):
        Creature.__init__(self, health, mana, dmg, absorb, lvl)
        self._stamina = stamina

    def refill_stamina(self, value):
        self._stamina += value

    def minus_stamina(self, value):
        self._stamina -= value


class Item(object):
    def __init__(self, health=0, mana=0, dmg=0, absorb=0, stamina=0, attack=0, defence=0, lvl=0):
        self._health = health
        self._mana = mana
        self._dmg = dmg
        self._absorb = absorb
        self._stamina = stamina
        self._attack = attack
        self._defence = defence
        self._lvl = lvl
    pass

creatures = {'', []}