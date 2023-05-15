class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(
        self.name, self.health, self.damage_per_attack)
    __repr__ = __str__


def declare_winner(fighter1: Fighter, fighter2: Fighter, first_attacker: str):
    while fighter1.health or fighter2.health > 0:
        if fighter1.name == first_attacker:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            fighter1.health -= fighter2.damage_per_attack
            print('1 : fighter1 health {} , fighter2 health {} '.format(
                fighter1.health, fighter2.health))
            if fighter1.health<=0:
                return fighter2.name    
        elif fighter2.name == first_attacker:
            print('2 : fighter1 health {} , fighter2 health {} '.format(
                fighter1.health, fighter2.health))

            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health<=0:
                return fighter1.name
        print('while loop : fighter1 health {} , fighter2 health {} '.format(fighter1.health,fighter2.health))
f1=Fighter("Harald", 20, 5)
f2= Fighter("Harry", 5, 4)
print(declare_winner(f1, f2, 'Harry'))
