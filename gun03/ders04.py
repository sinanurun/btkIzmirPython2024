meyve = ["elma","armut","üzüm","erik","çilek","karpuz"]

meyve.append("üzüm")
print(meyve)
print(meyve.count("üzüm"))
print(meyve.index("armut"))
meyve.insert(1,"kavun")
print(meyve)
meyve[3] = "kara üzüm"
print(meyve)
meyve.sort()
print(meyve)
meyve.reverse()
print(meyve)
liste2 = ["şeftali","muz"]
meyve.extend(liste2)
print(meyve)
liste3 = ["canerik","muşmula"]
meyve.append(liste3)
print(meyve)
meyve.pop()
print(meyve)
meyve.pop(2)
print(meyve)
meyve.remove("erik")
print(meyve)
meyve.clear()
print(meyve)
del meyve
print(meyve)

