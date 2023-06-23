# Problem 1
# Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

# liste = ["345","sadas","324a","14","kemal"]

# Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın.
# Bunu yaparken try,except bloklarını kullanmayı unutmayın.
liste = ["345", "sadas", "324a", "14", "kemal"]

for eleman in liste:

    try:
        eleman = int(eleman)  # Eğer hata ile karşılaşırsak burası hata verecek
        print(eleman)
    except:
        pass


# Problem 2
# Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın.
# Bu fonksiyon, eğer sayı çift ise *return* ile bu değeri dönsün.
# Ancak sayı tek sayı ise fonksiyon *raise* ile *ValueError* hatası fırlatsın.
# Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.

def cift_mi(sayi):
    if sayi % 2 == 0:
        return sayi
    else:
        raise ValueError


liste = [34, 2, 1, 3, 33, 100, 61, 1800]

for i in liste:
    try:
        print(cift_mi(i))
    except ValueError:
        pass
