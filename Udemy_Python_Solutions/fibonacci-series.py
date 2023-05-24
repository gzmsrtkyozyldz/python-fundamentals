# Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.
#
# 1,1,2,3,5,8,13,21,34...............
first_number = 1

second_number = 1

fibonacci = [first_number, second_number]
for i in range(10):


    first_number, second_number = second_number, first_number + second_number

    fibonacci.append(second_number)

print(fibonacci)
