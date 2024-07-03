# iç içe listeler, çok boyutlu listeler
sebze = ['domates', 'biber']
meyve = ['üzüm', 'çilek', 'kivi', 'karpuz', 'incir', 'ayva', 'armut', 'armut']
sark = ["peynir", "helva", "bal"]
yesillik = ["roka", "maydanoz", "tere"]
# pazar_listesi = sebze + meyve + sark + yesillik
# print(pazar_listesi)
# print(len(pazar_listesi))
pazar_listesi = [sebze, meyve, sark, yesillik]
pazar_listesi.append("baklava")
print(pazar_listesi)
print(len(pazar_listesi))
print(pazar_listesi[0])
print(pazar_listesi[0][0])
print(pazar_listesi[3][1])
for kategori in pazar_listesi:
    print(kategori)
    if type(kategori) != list:
        continue
    for urun in kategori:
        print(urun)