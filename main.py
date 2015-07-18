from environment import create_creatures, creature_dictionary, \
    hero_dictionary, create_hero, return_creature, fight

def ask_and_create(creature_type):
    def check_int(value):
        try:
            value = int(value)
            return True
        except ValueError:
            return False
    value_dict = {}
    if creature_type == "Creature":
        create_dictionary = creature_dictionary
    elif creature_type == "Hero":
        create_dictionary = hero_dictionary
    for value_type in create_dictionary:
        while True:
            value = raw_input("What {0} {1} will have?\n".format(value_type, creature_type.lower()))
            if check_int(value):
                value_dict[value_type] = value
                break
    if creature_type == "Creature":
        create_creatures(value_dict)
    elif creature_type == "Hero":
        create_hero(value_dict)

def print_fight():
    creature = return_creature("1")
    fight(creature)


def main():
    while True:
        result = raw_input("""
What do you want to do:
1 - Create creature
2 - Create hero
3 - Exit
""")

        if result == "1":
            ask_and_create("Creature")
        elif result == "2":
            ask_and_create("Hero")
        elif result == "4":
            print_fight()
        elif result == "3":
            break

    print "See you again later :)"


main()