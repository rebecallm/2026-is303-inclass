

class character: 
    def __init__(self, name, hp): 
        self.name = name 
        self.hp = hp

    def attack(self):
        return f"{self.name} attacks!"
    
    def __str__(self): 
        return f"{self.name} (HP:{self.hp})"
    
class Warrior (character):
    def __init__(self, name, hp, armor): 
        super().__init__(name, hp)
        self.armor = armor 
    
    def attack(self):
        return f"{self.name} swings sword!"
    
    def __str__(self): 
        base = super().__str__()
        return f"{base} [Armor: {self.armor}]"
    
class Mage (character):
    def __init__(self, name, hp, mana = 30): 
        super().__init__(name, hp)
        self.mana = mana 

    def attack(self):
        self.mana -= 5 
        return f"{self.name} casts a spell."
    
    def __str__(self): 
        base = super().__str__()
        return f"{base} [Mana: {self.mana}]"
    
class Healer(character): 
    def __init__(self, name, hp, heal_power): 
        super().__init__(name, hp)
        self.heal_power = heal_power 

    def attack(self):
        return f"{self.name} heals allies."
    
    def __str__(self): 
        base = super().__str__()
        return f"{base} [Heal power: {self.heal_power}]"  
    
party = [
    character("Village", 50),
    Warrior ("Aragorn", 120, 25),
    Mage ("Gandalf", 80, 200), 
    Healer ("Elrond", 90, 40)
]

for hero in party: 
    print(hero)
    print(hero.attack())
