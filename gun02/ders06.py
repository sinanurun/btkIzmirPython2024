#otoyol hız radar sistemi
yol = float(input("Kaç Km Yol  Gittiniz : "))
zaman = float(input("Kaç saat Yol  Gittiniz : "))
hiz = yol / zaman
if hiz > 132:
    print("cezayı yedin")
    print(f"{hiz-132} kadar ihlal ettiniz")
else:
    print("hız kurallarına uygun \ntebrikler")