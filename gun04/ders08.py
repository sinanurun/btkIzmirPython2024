import os
import time

dosya_adi = "deneme.txt"
with open(dosya_adi, "a") as dosya:
    dosya.write("esma")
with open(dosya_adi, "r") as dosya:
    print(dosya.read())

dosya_adi2 = "deneme2.txt"
if not(os.path.isfile(dosya_adi2)):
    dosya = open(dosya_adi2, "x")
    print("dosya oluşturuldu")
    dosya.close()
else:
    print("oluşturmak istediğiniz dosya mevcut")
time.sleep(5)
if os.path.exists(dosya_adi2):
  os.remove(dosya_adi2)
  print("dosya silindi")
else:
  print("The file does not exist")