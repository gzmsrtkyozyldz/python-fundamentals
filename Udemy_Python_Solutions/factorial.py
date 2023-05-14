# Bir sayının faktöriyel bulma
# Find the factorial of a number

print("""*******************
Faktoriyel Bulma Programı

Programdan çıkmak için 'exit' ya basın.
*******************""")
while True:
    sayi = input('Sayı:') # int çevirmedik çünkü exit gelmiş olabilir.
    if sayi == 'exit':
        print('Programdan kapanıyor...')
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1
        for i in range(2, sayi+1):
            faktoriyel *= i

    print('Faktoriyel:', faktoriyel)
