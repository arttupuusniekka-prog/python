# ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

#luetaan syötteet ja tallennetaan arvot muuttujiin.
eka = float(input("anna eka numero: "))
toka = float(input("anna toka numero: "))
kolmas = float(input("anna kolmas numero: "))
#float muuttaa numeeriseen muotoon jotta voidaan tehdä laskuja

#lasketaan summa, tulo ja keskiarvo
summa = eka + toka + kolmas
tulo = eka * toka * kolmas
keskiarvo = (eka + toka + kolmas)/3
#tulostetaan vastaus

print(f"Summa on {summa:.2f}")
print(f"Tulo on {tulo:.2f}")
print(f"Keskiarvo on {keskiarvo:.2f}")