# Problem 1
# Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.
# liste = ["345","sadas","324a","14","kemal"]

# Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın.
# Bunu yaparken try,except bloklarını kullanmayı unutmayın.
liste = ["345", "sadas", "324a", "14", "kemal"]

for eleman in liste:

    try:
        eleman = int(eleman)  # Eğer hata ile karşılaşırsak burası hata verecek ve print çalışmayacak.
        print(eleman)
    except:
        pass
