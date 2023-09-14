import random;

def coin_flip():
    return random.choice(["Heads", "Tails"]);

def die_roll():
    return random.randint(1, 6);
