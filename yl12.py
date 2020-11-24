puuviljad = ["omena",  "banan", "laim"]
print(puuviljad)
print(puuviljad[0])
puuviljad.append("sidrun")
print(puuviljad[3])
puuviljad[1] = "pirn"
print(puuviljad)
if "omena" in puuviljad:
    print("omena on listis")
else:
    print("omena ei ole listis")
print(len(puuviljad))
puuviljad.remove("omena")
print(puuviljad)
puuviljad.reverse()
print(puuviljad)
puuviljad.sort()
print(puuviljad)