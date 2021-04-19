import re
# Task 1. Replace all duplicated letters to one.

def dubl(str):
    res = re.sub(r'([a-z])\1+', r'\1', str)
    return res

print(dubl("aaaahhl"))
print(dubl("opqqqrstttvyy"))

# Task 2. Mus musculus -> M. musculus.

def short(name):
    newName = re.findall(r'^\w', name)[0] + "." + re.findall(r'\s\w+', name)[0]
    return newName

print(short("Mus musculus"))
print(short("Agalma elegans"))
print(short("Frillagalma vityazi"))
print(short("Cordagalma tottoni"))


# Task 3. Mus musculus (Y456) -> M.musculus Y456
def shorter(name, separator = " "):
    smth = re.findall(r'\w+', name)
    newName = re.findall(r'^\w', name)[0] + "." + separator.join(smth[1:])
    return newName

print(shorter("Mus musculus (Y456)"))
print(shorter("Agalma elegans (AB34)"))
print(shorter("Frillagalma vityazi"))
print(shorter("Cordagalma tottoni"))


#Task 4. Using Prosite.
pattern = r'K[K|R]CGH[L|M|Q|R]'

file = open("/Users/maria/Desktop/input.txt")
fasta = file.read().replace("\n", "")
file.close()

activeSite = re.search(pattern, fasta)
activeSiteStart = activeSite.start()

print(f'Isocitrate lyase GHI00594.1 contains its active site {activeSite[0]} starting from {activeSiteStart}'
      'th position.')
