# ohjelma, joka kysyy ympyrän säteen, ja laskee
# sen perusteella ympyrän pinta-alan
import math

#luetaan syöte ja tallennetaan arvo muuttujaan.
säde = float(input("anna ympyrän säde: "))

#float muuttaa numeeriseen muotoon jotta voidaan tehdä laskuja

#lasketaan pinta-ala
ala = (math.pi)*säde**2

#tulostetaan vastaus
#print("Pinta-ala on" + str(ala))
print(f"Pinta-ala on {ala:.2f}")