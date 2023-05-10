# Nested Lists
# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
# Input Format
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.
# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.
# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# Sözlükler veya İngilizce ismiyle dictionaryler aynı gerçek hayattaki sözlükler gibi davranan bir veritipidir. Bu veritipi, şimdiye kadar gördüğümüz tüm veritiplerinden yapısı gereği farklıdır. Sözlüğün içindeki her bir eleman indeks ile değil, anahtar (key), değer (value) olarak tutulur. Bu anlamda gerçek hayattaki sözlüklere oldukça benzerler. Örneğin, elimize bir ingilizce-Türkçe sözlük alıp freedom kelimesini(key ya da anahtar) aradığımız zaman karşılık değer özgürlük (değer ya da value) olarak karşımıza çıkar. Sözlükleri de bu şekilde düşünebiliriz.
# Süslü Parantez ve iki nokta (:) ile anahtar değerlerimizi yerleştirelim.
# sozluk = {"sıfır": 0, "bir": 1,"iki": 2,"üç": 3}
# print(sozluk)
# output => {'sıfır': 0, 'bir': 1, 'iki': 2, 'üç': 3}
#There are students in this class whose names and grades are assembled to build the following list:

#python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#The lowest grade of 37.21 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
students = {}
scores = []
for _ in range (int(input('n:'))): #first using=> lopping ten times using _second using=>terating over a list using _
    name = input()
    score = float(input())
    if score in students:
        students[score].append(name)
    else:
        students[score] = [name]
    if score not in scores: #this is for same score
        scores.append(score)
second = sorted(scores)[1]
students[second].sort()
for i in students[second]:
  print(i)