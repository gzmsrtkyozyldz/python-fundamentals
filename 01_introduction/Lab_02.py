# region Documantation
"""
#Karar Mekanizması ( if-else-elif)
# Uygulama içerisindeki karar mekanizmaları ile belirli bir şart tutması ya da tutmaması durumununa göre farklı kod bloklarının çalışmasını temin eden yapıdır.
# if kullanımı
if şart_cümlesi:
     kod_bloğu
else:
      kod_bloğu
"""
# endregion
# region Example 1 if-else
"""

sayi_1 = int(input("Sayı girin:"))
sayi_2 = int(input("Sayı girin:"))

if sayi_1 > sayi_2:
    print(f'{sayi_1} büyüktür')
else:
    print(f'{sayi_2} büyüktür')
"""
# endregion
# region Example 2 if-else
"""
#kullanıcıdan alınan sayı çift mi tek mi?
    sayi = int(input("Lütfen sayı giriniz: "))
mod = sayi % 2

if (mod == 0):
    print("Sayı Çift")
else:
    print("Sayı Tek")
"""
# endregion
#region Example 3 Weather
"""
# kullanicidan mevsim bilgisi alalim alinan mevsim bilgisine gore aylari ekrana yazdiralim
#mevsim = input("Lutfen bir mevsim giriniz: ").lower() #burada kullanilan lower() python icerisinde built in olan
# bu fonksiyon ile kullanicidan alinan inputu kucuk harfe donusturduk
#mesaj = " "
#if mevsim == "kis":
#    mesaj = "Aralik - Ocak - Subat"
#elif mevsim == "ilkbahar":
#    mesaj = "Mart - Nisan - Mayis"
#elif mevsim == "yaz":
#    mesaj = "Haziran - Temmuz - Agustos"
#elif mevsim == "sonbahar":
#    mesaj = "Eylul - Ekim - Kasim"
#else:
#    mesaj = "Boyle bir mevsim yok!"
#print(mesaj)
"""
#endregion
# region Example 4 Vehicle Type and Punishment
"""
arac_turu = int(input('Araç türü: '))
hiz = int (input('Hız:'))
if arac_turu == 'otomobil':
    if hiz >= 60:
        print('Cezalısınız..!')
    else:
        print('Ceza yok..!')
elif arac_turu == 'motorsiklet':
    if hiz >= 120:
        print('Cezalısınız..!')
    else:
        print('Ceza yok..!')
elif arac_turu == 'kamyon':
    if hiz >= 30:
         print('Cezalısınız..!')
    else:
        print('Ceza yok..!')
else:
    print('Lütfen doğru araç türü giriniz..!')

"""
# endregion
# region Example 5 Car Service
"""
# Kullanıcıdan aracının trafikte olduğu gün sayısını alıyoruz. 
# 365 günün altında ise 1.servis yılında 365 ve 365*2 aralığında ise 2.servis aralığında 365*2 ve 365*3
# ise 3. servis aralığında değilse aracını artık değiştir fosil olmuş.
Gun_sayisi = int(input("Aracınız kaç gündür trafikte: "))
if Gun_sayisi <= 365:
    print("Aracınız 1. servis yılındadır.")
elif Gun_sayisi > 365 and Gun_sayisi <= 365*2:
    print("Aracınız 2. servis yılındadır.")
elif Gun_sayisi > 365*2 and Gun_sayisi >= 365*3:
    print("Aracınız 3. servis yılındadır.")
else:
    print("Lütfen geçerli bir değer giriniz!")
"""
# endregion
# region Example 6 Finding the root of a 2nd degree equation(1)
"""
print("2.Dereceden Bir Denklemin Kökünü Bulma\n")
# y=ax^2+bx+c
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("denklemin reel kökü yok.")
elif delta == 0:
    print("birinci kök = ikinci kök :", (-b / 2 * a))
else:
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    print("Birinci Kök : {}\nİkinci Kök : {}".format(x1, x2))
"""
# endregion
# region Example 7 Finding the root of a 2nd degree equation(2)
"""
import math yazip math.sqrt() seklinde de yazabiliriz.
# from math import sqrt
# a = int(input("Birinci katsayi: "))
# b= int(input("Birinci katsayi: "))
# c= int(input("Birinci katsayi: "))
# diskriminant = b ** 2 - 4 * a * c
# Not: pythonda aritmetiksel islemler icn moduller var. Bu modulun adi "math". Karekok icin sqrt()fonksiyonundan kullanacağız
# if diskriminant > 0:
#     x1 = -b - sqrt(diskriminant) / 2 * a
#     x2 = -b - sqrt(diskriminant) / 2 * a
#     print(f'2 reel kok bulunmaktadir.\n birinci reel kok ==> {x1}\n ikinci reel kok ==> {x2}')
# elif diskriminant == 0:
#     x1 = -b - sqrt(diskriminant) / 2 * a
# elif diskriminant < 0:  #else durumu icin sart kosmayip bu satirada else diyebilirdik!
#     print("reel kok bulunmamaktadir.")
"""
# endregion
# region Example 8 Compare
# kullanicidan alinan 3 tane sayiyi buyukluk olarak karsilastiralim
# a = int(input("Sayi giriniz: "))
# b = int(input("Sayi giriniz: "))
# c = int(input("Sayi giriniz: "))
# if a > b and a > c:
#     print(f"{a} diger sayilardan buyuktur..")
# elif b > a and b > c:
#     print("{} diger sayilardan buyuktur.".format(b))
# elif c > a and c > b:
#     print("{} diger sayilardan buyuktur.".format(c))
# else:
#     print("Sayilardan bazilari birbirinden buyuk olabilir.")
# endregion
# region Example 9 Homework Midterm Final
"""
vize = input('Vize Notunuz : ')
final = input('Final Notunuz : ')
odev = input('Ödev Notunuz : ')

ortalama=(float(vize)*0.3)+(float(final)*0.6)+(float(odev))
print("Ortalama :{0} ".format(ortalama))
if(ortalama<50):
      print("Kaldınız")
else:
      print("Geçtiniz")
"""
# endregion
# region Example 10 BKE
"""
ame = input(('Adınız:')) #Gizem Sertkaya Özyıldız
pwd = input('Şifre: ')
#Login İşlemi
# Kullanıcının ilk adı ve şifresi ile login olsun.İsim birden fazla kelime içerebilir. Bu yüzden bize gelen string ifade içerinde bulunan boşluk karakterinden ifademizi aşağıda split ediyoruz yani parçalıyoruz. split() fonk. bizden aşağıda ki kullanımında bir parametre istedi bizde burada boşlık karakaterini kulandık. split() işini bitirdikten sonra bize bir liste döndü. Bu elde ettiğimiz listeyide 'name list' isimli değişkene atadık.
# name_lst listesinin index değerlerinde bulunan ifadelere istediğim gibi erişilebilir.sıfırıncı indexte tutulan değeri print ettik
#Artık login işlemi için ihtiyaç duyulan ilk ad elimizde. Login işlemine başlayabiliriz.
if name_lst[0].lower() == 'gizem' and pwd == '123':
      kg = float(input("kilo: "))
#     hg = float(input("Boy: "))
#     bmi = kg/(hg/100)**2
#     if 0 <= bmi <=18.5:
#         print(f'{name},{bmi} kilo degerlendirmen zayif..')
#     elif 18.6 <= bmi <= 24.9:
#         print("{} , {} kilo degerlendirmen normal..".format(name,bmi))
#     elif 25 <= bmi <= 29.9:
#         print("{} , {} kilo degerlendirmen kilolu..".format(name,bmi))
#     elif 30 <= bmi <= 35:
#         print("{} , {} kilo degerlendirmen fazla kilolu..".format(name,bmi))
#     elif 36 <= bmi <= 39.9:
#         print("{} , {} kilo degerlendirmen obez..".format(name,bmi))
#     else:
#         print("bilgilerinizi kontrol ediniz!")
# else:
#     print("Kullanici bilgileriniz hatali..")
"""
# endregion
# region Example 11 Product
"""
product = input("urun giriniz: ")
 if product == "muz" or product =="ananas" or product == "elma"
     print("Sebze reyonu")
elif product == "tv" or product =="pc" or product == "telefon"
     print("Teknoloji reyonu")
 else:
    print("Aradiginiz urun bulunmamaktadir!")
"""
# endregion
# region Example 12 Books
"""
kitap_sayisi = int(input("Kitap sayisi: "))
 if 0<=kitap_sayisi<=20:
     print(f'alinan kitap sayisi {kitap_sayisi}\ntoplam odenecek tutar{kitap_sayisi * 5 * 0.95}')
 elif 21<=kitap_sayisi<=50:
     print(f'alinan kitap sayisi {kitap_sayisi}\ntoplam odenecek tutar{kitap_sayisi * 5 * 0.90}')
 elif 51<=kitap_sayisi<75:
     print(f'alinan kitap sayisi {kitap_sayisi}\ntoplam odenecek tutar{kitap_sayisi * 5 * 0.85}')
 elif 76<=kitap_sayisi<=100:
     print(f'alinan kitap sayisi {kitap_sayisi}\ntoplam odenecek tutar{kitap_sayisi * 5 * 0.75}')
 else:
     print("kitap sayisini dogru giriniz>>") 
"""
# endregion





