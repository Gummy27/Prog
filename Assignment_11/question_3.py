def main():
    # Main functionality - DO NOT change this
    n = int(input("How long is the sequence(>0): "))
    fibo_tuple_recursion(n, (0, 1))

# Finish the function so it prints out the fibonacci sequence
def fibo_tuple(n):
    """
        This function generates the fibonacci sequence with a for loop.
    """
    a = (0, 1)
    for x in range(n):
        new_fib_number = sum(a)
        print(a[1], end=" ")
        a = (a[1], new_fib_number)

def fibo_tuple_recursion(n, new_fib):
    """
        This function generates the fibonacci sequence recursively
    """
    if(n != 0):
        print(new_fib[1], end=" ")
        fibo_tuple_recursion(n-1, (new_fib[1], sum(new_fib)))
    else:
        return
    

if __name__ == "__main__":
    main()