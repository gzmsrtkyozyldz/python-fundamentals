# region list documentation
"""
#Uygulama içerisinde anlık olarak bizim için değer tutan bir yapıdır. Birden fazla tipte farkı tipte değer tutabilir. Listeler RAM üzerinde tutulduğu için uygulama çalıştığı sürece üzerine yeni eklenen değerleri saklarlar. Yani uygulama kapatıldığında ilk yaratıldığı hale döner.
#Örneğin bir futbol takımları listem olsun.

# = ['Beşiktaş', 'Galatasaray', 'Adanademir Spor']
#Uygulama çalıştırıldığında bu liste tam olarak yukarıda ki yapıda Ram'in Heap alanına çıkartılır.
#Uygulama run timeda yani çalışıyorsa.Aşağıdaki kod çalıştığını varsayalım.
#Artık listem 4 elemanlalı. Lakin uygulama shutdown edildiğinde ilk yaratıldığı hale geri dönecektir. Çünkü listeler Ramde saklanır.
#Listeler inde mantığı ile çalışır yani listenin birinci elemanın erişmek istersem
#futbol_takimları[0] devam gerekemektedir.
"""
# endregion
# region Example Insert and Clear
"""
top_boxers.insert(3, 'Floyd Mayweater')
print(top_boxers)
top_boxers= ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis', 'Evander Holyfiled', 'Rocky Marciano']
top_boxers.clear(top_boxers)
print(top_boxers)
"""
# endregion
# region Example Movies
"""
movies = ['Fight Club', 'Matrix', 'Interstaller', 'Inception']
for film in movies:
    print(film)
for i in range(0, len(film)):
    print(film[i])
"""
# endregion
# region documentation
#clear() => fonk. listenin alayını siler.
#top_boxers.clear()
#pop() => verilen index değerindeli elemanı siler.
#current_boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis']
#top_boxers.extend(current_boxers]
# endregion
# region Example
"""
#2 farklı liste içerisine random olarak 10 adet sayı ile dolduralım.
#Sayılar 0-100arasında üretilsin.
#ilk adımda doldorulan bu iki listenin karşılıklı gelen index değerleri toplanarak 3.bir listeye eklesin.
#Lütfen soruyu index mantığıyla çözelim.

from random import randint
lst_1 = []
lst_2 = []
lst_3 = []
for i in range(10):
    lst_1.insert(i, randint(0, 101))
    lst_2.insert(i, randint(0, 101))

    lst_3.insert(i, lst_1[i] + lst_2[i])
    print(f'{lst_1[i]} + {lst_2[i]} = {lst_3[i]}')
print(lst_3)
word = input('Bir kelime giriniz:')
"""
# endregion
# region Example Vowels
"""
lst = []
vowels = 'aeıioöuü' #sesli_harfler = liste oluşturarak TEKRAR YAZ #if karakter not in tekrar olunca ekleme
for i in word:
    if i in vowels:
        lst.append(i)
print(lst)
#ekleme print(f'Yakalanan boşluk sayısı: {bosluk_sayisi)']
"""
# endregion
# region Homework User Password Strong
"""
a = False
b = False
c = False
for character in password:
    if character.isdigit() == 0:
        a = True
    elif character.isupper() == 1:
        b = True
from string import punctuation
username = input('Kullancı adı giriniz:')
password = input('Şifre Giriniz:')
if len(password) >= 16:
    for i in password:
        pass
else:
    print('Şifre uzunluğu en az 16 karakter olmalıdır..')
a = False
b = False
c = False
for character in password:
    if character.isdigit() == 0:
        a = True
    elif character.isupper() == 1:
        b = True
    elif character in punctuation == 1:
        c = True
        
if a == True and b == True and c == True:
else:
    print('Şifre uygun değildir.')

"""
# endregion
# region list comprehension
#rakamlari bir listeye ekleme
#sayilar
#for i in range(10):
#   sayilar.append(i)
#print(sayilar)
#print([i for  i in range(10)])

#rakamlarin karesini listeye dolduralim.
#print([i*i for i in range(10)])

#0-100 arasinda 3 tam bolunen sayilarin karesini listeye dolduralim
#print([i*i for i in range(100) if i % 3 == 0])
# endregion



















