# region Example 1 While
"""
0-100 arasinda ki sayilari ekrana yazdiralim.
sayac = 0
while sayac <=100:
   print(sayac)
     sayac += 1
"""
# endregion
# region Example 2 Even and Odd

# 1-101 arasindaki cift ve tek sayilarin miktarini ekrana yazdiralim.
sayac = 1
cift_sayilar = 0
tek_sayilar = 0
 while sayac<101:
     sayac += 1
     if sayac % 2 == 0:
         cift_sayilar += 1
     else:
         tek_sayilar += 1
 print("1-101 arasinda {} tane cift sayi, {} tane tek sayi bulunmaktadir.".format(cift_sayilar,tek_sayilar))
# endregion
# region Example 3 Addition even and odd
# 1-1000 arasindaki cift ve tek sayilarin toplamini ekrana yazdiralim.
sayac = 1
ciftsayilarin_toplami = 0
teksayilarin_toplami = 0
while sayac<=1000:
if sayac % 2 == 0:
   ciftsayilarin_toplami += sayac
else:
    teksayilarin_toplami += sayac
    sayac += 1
print("1-1000 arasinda ki cift sayilarin toplami: {}\ntek sayilarin toplami: {}".format(ciftsayilarin_toplami,teksayilarin_toplami ))
#endregion
# region Example 4
# kulllanicidan bir islem turu alalim ('+','-',vb) ve 2 adet sayi uzerinden kullanicinin istedigi islemi
process_type_list = ["+","-","*","/","e"]
while True:
 process = input("Islem turu giriniz: ")
      if process in process_type_list:
         if process == "e":
             print("uygulama kapatiliyor..")
             break
         else:
             sayi1 = int(input("Birinci sayiyi giriniz: "))
            sayi2 = int(input("Ikinci sayiyi giriniz: "))
                 if process == "+":
                    print(" Sonuc {} ' dir.".format(sayi1+sayi2))
                 elif process == "-":
                    print(" Sonuc {} ' dir.".format(sayi1-sayi2))
                 elif process == "*":
                    print(" Sonuc {} ' dir.".format(sayi1*sayi2))
                 elif process == "/":
                    print(" Sonuc {} ' dir.".format(sayi1/sayi2))
                else:
print("{} islemi icin lutfen gecerli bir islem turu seciniz!".format(process))
#endregion
# region Example 5 datetime

# kullanicidan yil bilgisi alacaginiz bu yil bilgisi 1943 ile gunumuz yili arasinda ise buldunuz degilse
from datetime import datetime
started_date = 1943
search_date= int(input("aradiginiz yili giriniz: "))
while started_date <= datetime.now().year:
     if started_date == search_date:
         print("Bulundu.. Aradiginiz yil {}".format(started_date))
         break
     else:
         print("Aradiginiz {} yili bulunmamaktadir.".format(started_date))
    started_date += 1
#true false
from datetime import datetime
started_date = 1943
search_date= int(input("aradiginiz yili giriniz: "))
is_exist = False
while started_date <= datetime.now().year:
         if started_date == search_date:
           print("Bulundu.. Aradiginiz yil {}".format(started_date))
         is_exist = True
         break
     started_date += 1
if not is_exist:
     print("Aradiginiz tarih bulunmamaktadir.")
# endregion
# region Example 6
# tek sayilarin toplamini bulun continue kullanarak.0-101 arasinda
i = 0
sum = 0
while i<= 101:
     i +=1
     if i % 2 == 0:
         continue
     sum += i
     print(sum)
# endregion
# region Homework
#Kullanıcıdan tam adını alalım.
#isim.soyisim@harrypotter.com mail adresini oluşturalım ekrana basalım. split kullanalım.
name = input('Ad-Soyad:').lower()
name_lst = name.split(' ')

print(name_lst [0] + '.' + name_lst [-1] + '@harrypotter.com')
# endregion












