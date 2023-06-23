# Problem
# Given an integer, n, print the following values for each integer i from 1 to n:
# Decimal Octal Hexadecimal (capitalized) Binary The four values must be printed on a single line in the order specified above for each from to . Each value should be space-padded to match the width of the binary value of .
# Input Format
# A single integer denoting n.
# Output Format
# Print n lines where each line i (in the range 1 <= i <= n) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.

def print_formatted(number):

    width = len("{0:b}".format(number))  # Genişlik değişkeni sayının ikili temsilinin uzunluğu ile başlatılır
    # yazdırırken her bir değerin doldurulması gereken genişliği belirler

    for i in range(1, number + 1):  # For döngüsü 1'den sayı + 1'e en son dahil yinelenir
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
