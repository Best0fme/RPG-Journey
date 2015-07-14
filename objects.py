#This file will contain object structures

class Creature(Object):
    Health = "100"
    Mana = "100"
	Dmg = "100"
	Absorb = "100"
    pass

class Herro(Creature, Bag):
    Stamina = "100"
    pass


class Bag(Object):
    articles = []
    pass
