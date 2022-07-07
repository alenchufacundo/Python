socios = ["nicolas", "lucas", "pedro", "benjamin", "micaela", "belen","lorenzo"]
print(len(socios))
socios.append("agustina")

if(socios.count("pedro")) > 0:#al usar el count, dice que si encuentra un nº mayor a 0->hacer lo siguiente.
    socios.remove("pedro")
socios.insert(2,"carlos")
posicionBelen = socios.index("belen")
socios.insert(posicionBelen+1,"maria")
socios.sort()
print(socios)

while (socios.count("pedro")) > 0:
    socios.remove("pedro")