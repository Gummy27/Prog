# Your function definitions goes here
def sum_of_factors(num):
    factors_sum = 0

    for factor in range(1, num):
        if(num % factor == 0):
            factors_sum += factor

    return factors_sum

def decide(num):
    if(sum_of_factors(num) == num):
        return(f"{num} is a perfect number.")
    elif(sum_of_factors(num) < num):
        return(f"{num} is deficient.")
    elif(sum_of_factors(num) > num):
        return(f"{num} is abundant.")

print(decide(6))