"""
unosi se cetvorocifreni broj abcd
program printa poruku "super" ako je a c = b d
"""

broj = (input("Unesite cetvorocifreni broj "))

print(broj[0])
print(broj[1])
print(broj[2])
print(broj[3])
print(broj[::2])
print(broj[1::2])
if broj[::2] == broj[1::2]:
    print("super")
    