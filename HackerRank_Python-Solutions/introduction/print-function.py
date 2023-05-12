# Read an integer N.
# Without using any string methods, try to print the following:
# 123....N
# Note that "..." represents the values in between.
# Input Format
# The first line contains an integer 'N'.
# Output Format if n:5 is result '12345'
# Output the answer as explained in the task.
for i in range(1, int(input('n:')) + 1):
    print(i, end='')
