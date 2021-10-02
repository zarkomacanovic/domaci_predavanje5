"""
unosi se trocifreni broj
odrediti broj koji se dobija zamjenom prve i zadnje cifre
"""

broj = (input("Unesite trocifreni broj "))

cifra1 = int(broj[0])
cifra2 = int(broj[1])
cifra3 = int(broj[2])

broj2 = cifra3*100+cifra2*10+cifra1

print(broj2)