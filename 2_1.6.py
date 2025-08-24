#ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroinen koodi, jonka numerot väliltä 0-9.
#nelinumeroinen koodi, jonka numerot väliltä 1-6.

import random

numerot = list(range(0, 9))
koodi = random.sample(numerot, k=3)
print("koodisi on", koodi)

numerott = list(range(1, 6))
koodi = random.sample(numerott, k=4)
print("koodisi on", koodi)