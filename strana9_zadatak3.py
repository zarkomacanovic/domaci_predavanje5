"""
Unose se duzine stranica pravougaonika
program racuna obim i povrsinu pravougaonika
"""


a = int(input("Unesite duzinu prve stranice pravougaonika "))
b = int(input("Unesite duzinu druge stranice pravougaonika "))

obim_pravougaonika = (a+b)*2
povrsina_pravougaonika = a*b

print("Obim pravougaonika je ",obim_pravougaonika)
print("Povrsina pravougaonika je ", povrsina_pravougaonika)