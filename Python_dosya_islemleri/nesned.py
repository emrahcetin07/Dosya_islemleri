def islem(islem_adi):
    def toplama(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim=1
        for a in args:
            carpim *=a
        return carpim

    if islem_adi=="toplama":
        return toplama
    else:
        return carpma#fonksiyon return ediliyor

toplama=islem("toplama")
print(toplama(10,20))

