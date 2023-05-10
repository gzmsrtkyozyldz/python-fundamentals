# Consider a list (list = []). You can perform the following commands:
# 1. insert i e: Insert integer e at position i.
# 2 . print: Print the list.
# 3. remove e: Delete the first occurrence of integer e .
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of
# the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your
# list.
# Example
# N = 4
# append 1
# append 2
# insert 3 1
# print
# append 1: Append 1 to the list, arr = [1].
# append 2: Append 2 to the list, arr = [1, 2].
# insert 1 3: Insert 3 at index 1,arr = [1, 3, 2].
# print: Print the array.
N = int(input("N:")) # first step=> N=4
result = []
for i in range(N):
    my_list = input().split()
    if my_list[0] == 'insert':
        result.insert(int(my_list[1]),int(my_list[2])) #fourth step => write ' insert 1 3 '
    elif my_list[0] == 'print': #last step => write 'print'
        print(result)
    elif my_list[0] == 'remove':
        result.remove(int(my_list[1]))
    elif my_list[0] == 'append':  #second step=> write 'append 1' third step=> write 'append 2'
        result.append(int(my_list[1]))
    elif my_list[0] == 'sort':
        result.sort()
    elif my_list[0] == 'pop':
        result.pop()
    elif my_list[0] == 'reverse':
        result.reverse()

