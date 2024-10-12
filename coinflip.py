import random

def flip_coin():
    return random.choice(['heads', 'tails'])

if flip_coin() == 'tails':
    print ("The coin landed on TAILS.")
else:
    print ("The coin landed on HEADS.")