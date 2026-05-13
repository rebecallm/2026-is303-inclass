"""

Inputs: 
- A string containing an attribute guess or the guess of the animal's name. 

Processes: 
- Randomly select an animal (use import random)
- Allow the user to guess until they guess the correct animal.
- When they guesss, tell them if the animal has the attribute or not.
- Tell the user when they guess correctly. 

Output:
- Attribute guess correctness 
- Congratulations message. 

"""

import random              #Teach python how to do random stuff 

ANIMALS = {
    "Lion" : ["Mammal", "Four legs", "Predator", "Carnivore","Fur", 
              "Tail", "Sharp Teeth", "King of the jungle"],
    "Hyena" : ["Mammal", "Four legs", "Predator", "Carnivore", "Spots",
                "Fur", "Fast"],
    "Elephant" : ["Big", "Four legs", "Trunk", "Mammal", "Herbivore", "Tusks", 
                  "Tail", "Eats grass", "Africa", "Asia", "Transportation"],
    "Giraffe" : ["Tall", "Long neck","Four legs", "Mammal", "Herbivore", "Spots", 
                 "Fur", "Tail", "Africa", "Eats leaves",],
    "Zebra" : ["Four legs", "Mammal", "Herbivore", "Stripes", "Fur", 
               "Tail", "Africa", "Eats grass", "Yellow"], 
    "Cheetah" : ["Mammal", "Four legs", "Predator", "Carnivore", "Spots", 
                 "Fur", "Tail", "Fast","Africa", "Eats antelope"],
    "Panda" : ["Mammal", "Four legs", "Herbivore", "Black and White", 
               "Fur", "Tail", "Eats Bamboo", "China", "Endangered"],
    "Kangaroo" : ["Mammal", "Two legs", "Tail", "Pouch", "Herbivore", "Fur",
                  "Hops", "Australia",],
    "Penguin" : ["Bird", "Two legs","Snow", "Wings", "Swims", "Black and White", 
                 "Feathers", "Tail", "Beak"],
    "Dolphin" : ["Mammal", "Swims", "Intelligent", "Tail", "Fins", 
                 "Blowhole", "Echolocation"]
}

WELCOME_MESSAGE = """Animal guessing game 
I have picked a random animal. Guess an 
attribute or the name of the animal.
"""

CONGRATULATIONS_MESSAGE = "You won!"

list_of_animal_names = list(ANIMALS.keys())
random_animal = random.choice(list_of_animal_names)
random_animal_attributes = ANIMALS[random_animal]

print(WELCOME_MESSAGE)

guess = ""

while guess != random_animal: 
    guess = input("Please guess an attribute or the animal name: ").capitalize()
    if guess in random_animal_attributes:
        print(f"Yes, {guess} is an attribute of the animal.")
    elif guess == random_animal:
        print(CONGRATULATIONS_MESSAGE)
    else:
        print (f"No, {guess} is NOT an attribute of the animal.")

