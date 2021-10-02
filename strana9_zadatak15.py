"""
unosi se cetvorocifreni broj
odrediti broj koji se dobija zamjenom trece i druge cifre
"""

broj = (input("Unesite cetvorocifreni broj "))

cifra1 = int(broj[0])
cifra2 = int(broj[1])
cifra3 = int(broj[2])
cifra4 = int(broj[3])

broj2 = cifra1*1000+cifra3*100+cifra2*10+cifra4

print(broj2)