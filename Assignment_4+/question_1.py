max_num = int(input("Input maximum number: "))

for x in range(1, max_num+1):
    sum_of_digits = 0
    for i in str(x):
        sum_of_digits += int(i)
    
    if(sum_of_digits**3 == x):
        print(x)