# ohjelma, joka kysyy suorakulmion
# kannan ja korkeuden, ja laskee
# niiden perusteella pinta-alan, sekä piirin

#luetaan syötteet ja tallennetaan arvot muuttujiin.
kanta = float(input("anna suorakulmion kanta: "))
korkeus = float(input("anna suorakulmion korkeus: "))
#float muuttaa numeeriseen muotoon jotta voidaan tehdä laskuja

#lasketaan pinta-ala
ala = kanta * korkeus
piiri = kanta*2 + korkeus*2
#tulostetaan vastaus
#print("Pinta-ala on" + str(ala))
print(f"Pinta-ala on {ala:.2f}")
print(f"Pinta-ala on {piiri:.2f}")