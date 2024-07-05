try:
    a = int(input("Enter a number: "))
    print(a)
    # k = a/0
    z = "q"/"w"
except ValueError:
    print("hatalı veri girdiniz")
except ZeroDivisionError:
    print("hata olarak sıfıra bölme var uygulamada")
except Exception as e:
    print("Aldığınız hata tipi : ", e)
