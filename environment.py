import random
from objects import Creature, Hero

creature_dictionary = ["health","mana","dmg","absorb"]
hero_dictionary = creature_dictionary + ["stamina"]
creatures = {}
hero = None
def create_creatures(value_dict):
    health, mana, dmg, absorb = value_dict["health"], value_dict["mana"],\
    value_dict["dmg"], value_dict["absorb"]
    if not "1" in creatures:
        creatures["1"] = []
    creatures["1"].append(Creature(health, mana, dmg, absorb))

def create_hero(value_dict):
    global hero
    health, mana, dmg, absorb, stamina = value_dict["health"], value_dict["mana"],\
    value_dict["dmg"], value_dict["absorb"], value_dict["stamina"]
    print health, mana, dmg, absorb, stamina
    hero = Hero(health, mana, dmg, absorb, stamina)
    print hero

def return_creature(lvl):
    return random.choice(creatures[lvl])

def fight(creature, hero = hero):
    print "Fight began"
    while creature.alive() or hero.alive():
        print "Heroes turn"
        for skill in hero.skills():
            dmg = skill.deal_damage()
            if dmg:
                print "Hero made {0} damage".format(dmg)
                creature.minus_health(dmg)

        print "Creature's health is {0}".format(creature._health)

        if not creature.alive():
            print "Creature died"
            break

        print "Creature turn"
        for skill in creature.skills():
            dmg = skill.deal_damage()
            if dmg:
                print "Creature made {0} damage".format(dmg)
                hero.minus_health(dmg)

        print "Heroes health is {0}".format(hero._health)
        if not hero.alive():
            print "Hero died"
            break

        print "Fight is over"
