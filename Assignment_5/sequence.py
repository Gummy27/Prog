n = int(input("Enter the length of the sequence: ")) # Do not change this line

'''
The pattern is that the last 3 numbers are summed up to generate the next one.

The algorithm will first print out the first 3 numbers as they are essential to 
"kick off" the pattern.

We will initialize a list which will have the 3 last numbers. In a for loop
the list is summed up and stored in a variable. That variable is printed out 
as the next number. Then we will pop the first value in the list and append the
new sum into the list.
'''

print("1 2 3", end=" ")
last_three_numbers = [1, 2, 3]
for x in range(4, n+1):
    new_sum = sum(last_three_numbers)
    print(new_sum, end=" ")
    last_three_numbers.append(new_sum)
    last_three_numbers.pop(0)
print()
