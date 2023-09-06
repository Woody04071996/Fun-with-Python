#przypadkowe slowa
#losowosc

import random

print("\nWitaj w losowaniu slow !!!!")

WORDS = ["samochod", "rower", "hulajnoga", "motor", "lodz" ]


while WORDS:
    los = random.choice(WORDS)
    print(los)
    WORDS.remove(los)
    
    


    










