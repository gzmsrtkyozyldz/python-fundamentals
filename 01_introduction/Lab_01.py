# region Documantation
"""
Değişken (variable)
Yazılım dillerinde değişkenleri kutulara benzetebiliriz.
Diğer programlarda dillerinde değişken tanımlarken ilk önce değişkenin tipi sonra adını ve sonrada üzerine değer atarız
 int x = 10
Pythonda değişken tanımlarken herhangi bir tip belirtmiyoruz.
 x = 10
Bir tip belirtmediğimiz için değişkenimiz anlık olarak içerisine atılan değerin tipine bürünmektedir.
 x = "severus snape"
Buradan print() bulit-in fonk. aracığıyla ile değişken üzerinde tutulan ifadeyi ekrana yazdırdık.
Yukarıdaki iki satırın first_name değişkeni içerisinde 10 değerini atadık.
Kullanıcıdan alınan 2 adet sayı üzerinden temel 4 işlem yapan uygulama
Kullanıcıdan input alırken python içerisindeki built-in olarak bulunan input() fonk. kullanıyoruz. Daha sonra kullanıcıya doğru yönlendirmek için içerisine bir mesaj yazıyoruz.
 Lakin şunu unutmayalım kullanıcıdan her değer aldığımızda bize gelen valuenun tipi string.Aritmatiksel işlem yaptırmak istediğimizde bize gelen değeri değişken
 tipine dönüştürmemiz gerekmektedir.
"""
# endregion
# region Example 1

#Arithmetric opetors
sayi_1 = int(input("Lütfen bir sayı giriniz: "))
sayi_2 = int(input("Lütfen bir say giriniz: "))
toplam = sayi_1 + sayi_2
print(f' Sonuç: {toplam}')
carpma = sayi_1 * sayi_2
print(f'{} x {} ={}' .format(sayi_1, sayi_2, carpma))
bolme = sayi_1 / sayi_2
print(bolme)
cikarma = sayi_1 - sayi_2
print(f'Cikarma isleminin sonucu: {cikarma}')

# endregion
# region Example kare alan ve çevre
#Karenin çevresi ve alanı
#Yukarıda kullanıcıdan alınan input int()fonksiyonu aracığıyla int tipine dönüştürdük çünkü kullanıcıdan gelen değeri aritmatiksel işleme girmesi için.
karenin_kenari = int(input("Karenin kenarını giriniz: "))
alan = karenin_kenari * karenin_kenari
print(f' Alan Sonuç:  {alan}')
cevre = 4 * karenin_kenari
print(f' Çevre Sonuç: {cevre}')

#endregion
# region Example dikdörtgen alan ve çevre

Kullanıcıdan alınan kısa ve uzun kenar dikdörtgen alan ve çevre
kisa_kenar = int(input("Kısa kenarı giriniz: "))
uzun_kenar = int(input("Uzun kenarı giriniz: "))
cevre = (2 * kisa_kenar) + (2 * uzun_kenar)
alan = kisa_kenar * uzun_kenar
print(f'Çevre Sonuç: {cevre}')
print(f'Alan Sonuç:{alan}')

# endregion
# region Example üçgen alan
#Üçgenin alanını hesaplayalım.
base = int(input("Taban: "))
height = int(input("Yükseklik: "))
print(f'Üçgenin Alanı: { (base * height) / 2 }')
# endregion
# region Example kare çevre ve alan
# Kullanicidan alinan kenar bilgisine gore bir karenin alanini ve cevresini hesaplayin
kenar = int(input("kenari giriniz:"))
karenin_cevresi = kenar * 4
karenin_alani = kenar * kenar
print(f'cevresi: {karenin_cevresi}')
print(f'alan: {karenin_alani}')
# endregion




















