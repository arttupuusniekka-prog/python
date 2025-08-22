# ohjelma, joka kysyy käyttäjältä massan
# keskiaikaisten mittojen mukaan leivisköinä,
# nauloina ja luoteina. Ohjelma muuntaa syötteen
# täysiksi kilogrammoiksi ja grammoiksi sekä
# ilmoittaa tuloksen käyttäjälle.

luoti: float = 13.3
naula: float = 32*luoti
leiviskä: float = 20*32*luoti
#luetaan syötteet ja tallennetaan arvot muuttujiin.
leiviskät = float(input("anna leiviskät: "))
naulat = float(input("anna naulat: "))
luodit = float(input("anna luodit: "))
#float muuttaa numeeriseen muotoon jotta voidaan tehdä laskuja

#lasketaan määrä
grammat = (luoti*luodit + naula*naulat + leiviskä*leiviskät) % 1000
kilot = (luoti*luodit + naula*naulat + leiviskä*leiviskät)//1000

#tulostetaan vastaus

print(f'Vastaus on {kilot} kilogrammaa ja {grammat: .2f} grammaa')


