# region Documantation
"""
# For Loop
# For loop geçmeden önce incelememiz gerek birkaç tane yardımcı operatör ve fonksiyon bulunmaktadır. Bunlar "in" & "not in" ayrıca range() fonksiyonudur.
# in operatörü bir liste içerisinde aranan ifade geçiyorsa True geçmiyorsa False döner. Şunu unutmayalım string ifadelerde karakter dizileridir yani string ifadeye  in operatörünü kullanabiliriz.
# not in operatörü ise in operatörünün tam tersi mantıkta çalışır aranan ifade geçmiyorsa True geçiyorsa False döner.
#name = 'Mike Tyson'
#print('b' in name)

# range() fonk. for loop ile sıklıkla kullanılan bir yapıdır.
# range(100) fonk. içerisine burada old. gibi 100 değerini verirsek bize 0-99 arasında tam sayı listesine döner.
# unutmayın range içerisine bir argüman verildiğinde verilen argüman "n" kabul edersek "n-1" kadar çalışır. Ayrıca yine aynı senaryoda range default olarak sıfırdan başladı. Biz aksini söylemediğimiz sürece range default olarak hep sıfırdan başlayacaktır.

# for i in range(10):
# print(i) #burada print()fonk. değerleri alt alta yazmaktadır. Bunu yanyana yazdırmanın yolunu bulun.
# for i in range(1,11):
# print(i,end=" ")
#range () fonk. 2 argüman verirsek örneğin 5 ile 10, 5ten başlayarak 10 kadar bir sayı listesi döner.
#for i in range(5, 10):
#print(i)
#range() 3 argüman verirsek,1. argüman başlangıç,ikinci argüman bitiş, üçüncü argüman ise adım miktarını temsil eder.
#for i in range(1, 21, 2):
#   print(i)
#1-100 arasındaki çif ve tek toplamı
"""
# endregion
# region Example 1 even
um_even = 0
sum_add= 0
for i in range(1,101):
     if i % 2 == 0:
        sum_even += i
    else:
        sum_add += i
print(f'Çift sayıların toplamı:{sum_even}\nTek sayıların toplamı: {sum_add} ')
# endregion
#region Homework
#Kullanıcıdan başlangıç ve adım miktarlarını alalım. Bu şartlara bağlı kalarak her bir adımdaki sayının karesi alarak ekrana yazalım.
#çıktıyı şu formatta istiyorum 1. adımdaki sonuç:9,16,25
baslangic = int(input("Sayı giriniz: "))
bitis = int(input("Sayı giriniz: "))
adim = int(input("Adım miktarı: "))
counter = 1
for item in range(baslangic, bitis, adim):
    print(f'{counter}. adımda ==> {item ** 2}')
    counter += 1
# endregion
# region Example 2 is_prime
#Kullancıdan alınan sayı asal mı değil mi?
sayi = int(input('sayı: '))
asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2, sayi):
    if sayi % i == 0:
        asalmi = False
        break

if asalmi:
    print('sayı asaldır.')
else:
    print('sayı asal değildir.')
# endregion
# region Example 3 Counter
#0-1000 arasındaki sayıları 10'ar dolaşalım 10'ar toplayalım Her bir adımda ki sayıları toplayarak toplamı kullanıcya gösterelim.
i = 0
counter = 1
for i in range(0, 1001, 10):

    print(f'{counter}. adımda ==>  {i}')
    counter += 1
# endregion
# region Example 4 The Multiplication Table
#çarpım tablosu 1den 10'a kadar iç içe for loop
for i in range(1, 11):
    print("---------")
    for j in range(1, 11):
        print("{} * {} = {}".format(i, j, i * j))
# endregion
# region Example 5 kare
#'*' sembollerini kullanarak kare sembolü
kenar = int(input("kare kenar sayısını giriniz -> "))
for i in range(0, kenar):
  for j in range(0, kenar):
    print('*', end='')
  print(' ')
# endregion
# region Example 6 üçgen
  #* dik üçgen yapın
kenar = int(input("üçgen kenar sayısını giriniz -> "))
for i in range(0, kenar):
  for j in range(0, kenar):
      if j <= i:
         print('*', end='')
  print(' ')
# endregion
# region Example 7 Append
liste = [ ]
for i range (0, 10):
    liste.append(i)
print(liste)
# endregion
# region Example 8 Random Number
from random import randint
lst = []
for i in range(0, 10):
    random_number = randint(0, 101)
    lst.append(random_number)
print(lst)
# endregion
# region Example 9 Mod 3 and **
#-100 arasında rastgele 10 adet sayı üretilen sayılardan 3 tam bölünenleri karesi
from random import randint
lst = []
for i in range(0, 10):
      random_number = randint(0, 101)
      if i % 3 == 0:
         print(random_number)
         lst.append(random_number)
print(lst)
# endregion
# region Homework
#kullanıcıdan bir söz öbeği alalım
#örneğin merhabalar ben burak yılmaz
#yukarıda ki örnek söz öbeğinde ki her bir harfi bir listeye ekleyelim
#yol 1
#söz öbeği içerisinden adım adım dolaşarak
#if word[i] != ' ':
#lst.append word[i]) TEKRAR YAP BUNUNLA
#yol 2
#söz öbeğinde ki her bir harfi döngüye itarate ederek yapın

a = []
name = "Merhabalar Ben Dumbledore"
for i in range(0, len(name)):
    a.append(name[i])
print(a)
#yol 2
#söz öbeğinde ki her bir harfi döngüye itarate ederek yapın TEKRAR YENİDEN YAZ

for character in word:
    if character in word != ' ':
        lst.append(character)
print(lst)
"""
# endregion


















