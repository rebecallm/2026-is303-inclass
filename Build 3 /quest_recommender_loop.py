'''
Inputs: 
player class (string)
player level (integer)

Processes:
Suggest a quest type based on the player's class and level.
Different quests for level ranges (1-10, 11-25, 26+)
Modified by class (warrior, mage, rogue)

Outputs:
A recommended quest type (string)

'''
class_types = {
    "Wizard" : ["Find a wand", "Find a spellbook", "Duel your professor"],
    "Fighter" : ["Find a sword", "Find a shield", "Defend your professor"]
}

# Find a specific quest in the data structure
quest_to_find = input("What quest are you looking for? ")

for class_key in class_types: 
    class_quests = class_types[class_key]
    for quest in class_quests:
        if quest == quest_to_find:
            print (f"Ypur quest is performed by the {class_key}")

player_class = input("What is your class? ").capitalize()
player_level = ""
while not player_level.isdigit():
    player_level = input("What is your current level? (enter a number) ")

player_level = int(player_level)

# Calculate quest level based on the player level 
quest_level = 0 
if player_level >=26:
    quest_level = 2
elif player_level >= 11: 
    quest_level = 1

recommended_quest = class_types[player_class][quest_level]
print (f"You should do this quest: ")

users_class_quests = class_types[player_class]
print(users_class_quests)
quest_by_level = users_class_quests[quest_level]
print(quest_by_level)



