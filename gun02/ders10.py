# tek satırda koşullu ifadeler
a = 5
if a > 4:
    b = "büyüktür"
else:
    b = "küçüktür"

print(a, b)

c = "büyüktür" if a>4 else "küçüktür"
print(a,c)

print("büyüktür" if a>4 else "küçüktür")
