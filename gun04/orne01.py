def sinifOrtalama(*args):
    toplam = 0
    for arg in [*args]:
        toplam += arg
    ortalama = toplam / len(args)
    return ortalama
if __name__ == '__main__':
    print(sinifOrtalama(1,5,9,8,7,4))