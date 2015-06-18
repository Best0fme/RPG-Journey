def abs(value):
    if value <= 0:
        return 0
    else:
        return value

import random
import time

hero = {'HP' : [100, 100], 'Stamina' : [100, 100], 'Prey' : [0, 1]}

bag = {'Sword' : [3, 5, 0], 'Shield' : [2, 3, 0]}

troll = {'HP' : [60, 60], 'Atack' : [1, 10], 'Deffence' : [2, 2]}

hero_battle = {'HP' : hero.get('HP'), 'Atack' : bag.get('Sword')[0:2],
               'Deffence' : bag.get('Shield')[0:2]}
print 'You meet Troll battle began'
while troll.get('HP')[0] > 0 and hero_battle.get('HP')[0] > 0:
    damage_npc = abs(random.randint(troll.get('Atack')[0],
                                troll.get('Atack')[1]) - random.randint(hero_battle.get('Deffence')[0],
                                                                        hero_battle.get('Deffence')[1]))
    damage_hero = abs(random.randint(hero_battle.get('Atack')[0],
                                 hero_battle.get('Atack')[1]) - random.randint(troll.get('Deffence')[0],
                                                                               troll.get('Deffence')[1]))

    print 'Troll made',damage_npc,'damage'
    hero_battle.get('HP')[0] = abs(hero_battle.get('HP')[0] - damage_npc)
    print 'Heroes HP is',hero_battle.get('HP')[0]
    print ''
    print 'Hero''s made',damage_hero,'damage'
    troll.get('HP')[0] = abs(troll.get('HP')[0] - damage_hero)
    print 'Troll''s HP is',troll.get('HP')[0]
    print ''
    time.sleep(2)

if troll.get('HP')[0] <= 0:
    print 'Troll died'

if hero_battle.get('HP')[0] <= 0:
    print 'Hero died'

raw_input('Type Enter to leave!')    
    
