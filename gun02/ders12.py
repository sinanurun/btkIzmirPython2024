gun = input("gün değerini giriniz")
match gun:
    case "pazartesi":
        print("birinci")
    case "salı":
        print("ikinci")
    case _:
        print("tanımsız gün")

