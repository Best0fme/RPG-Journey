#This file will contain object structures
class Skill(object):
    current_cool_down = 0
    def __init__(self, dmg=0, cool_down=0):
        self._dmg = dmg
        self._cool_down = cool_down

    def check_availability(self):
        if self.current_cool_down == 0:
            return True
        else:
            return False

    def calc_damage(self):
        return self._dmg

    def move_cool_down(self):
        if self.check_availability():
            self.current_cool_down = self._cool_down
        else:
            self.current_cool_down -= 1

    def deal_damage(self):
        if self.check_availability():
            self.move_cool_down()
            return self.calc_damage()
        else:
            self.move_cool_down()
            return None

class Creature(object):
    def __init__(self, health=0, mana=0, dmg=0, absorb=0):
        self._health = health
        self._mana = mana
        self._dmg = dmg
        self._absorb = absorb
        self._skills = [Skill(dmg, 1)]

    def refill_health(self, health):
        self._health += health

    def minus_health(self, health):
        self._health -= health

    def alive(self):
        if self._health <= 0:
            return False
        return True

    def skills(self):
        return self._skills



class Bag(object):
    _articles_off = []
    _articles_on = []

    def wear_item(self, item_index, hero):
        if item_index._lvl <= hero._lvl:
            __value = self._articles_off.pop(item_index)
            self._articles_on.append(__value)

    def strip_item(self, item_index):
        __value = self._articles_on.pop(item_index)
        self.articles_off.append(__value)


class Hero(Creature, Bag):
    def __init__(self, health=0, mana=0, dmg=0, absorb=0, stamina=0):
        Creature.__init__(self, health, mana, dmg, absorb)
        self._stamina = stamina

    def refill_stamina(self, value):
        self._stamina += value

    def minus_stamina(self, value):
        self._stamina -= value


class Item(object):
    def __init__(self, health=0, mana=0, dmg=0, absorb=0, stamina=0, attack=0, defence=0):
        self._health = health
        self._mana = mana
        self._dmg = dmg
        self._absorb = absorb
        self._stamina = stamina
        self._attack = attack
        self._defence = defence