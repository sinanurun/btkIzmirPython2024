#default parametreli fonksiyonlar
# def kare(a=5):
#     return a*a
#
# print(kare(2))
# def daireAlan(r=1, pi= 3.14):
#     alan = pi * r * r
#     return alan
#
# alan = daireAlan(5, 3)
# print(alan)

def silindirHacim(r=1, h=1, pi=3.14):
    hacim = pi * r * r* h
    return hacim

hacim = silindirHacim(5, 3.15)
print(hacim)