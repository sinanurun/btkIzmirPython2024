import datetime
from datetime import datetime
import time
# print("merhaba dünya")
# time.sleep(5)
# print("sana da merhaba")
a = input("birinci giris")
giris = datetime.now()
print(giris)
b = input("ikinci giris")
giris2 = datetime.now()
fark = giris2 - giris
print(fark)
print(fark.total_seconds())