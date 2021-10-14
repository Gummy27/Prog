def main():
    int_list, input_correct = user_input()
    if(input_correct):
        sorted_list = sorted(int_list)
        
        composite_list = []
        for x in sorted_list:
            if(not is_prime(x)):
                if(x not in composite_list):
                    composite_list.append(x)

        min_in_list = min(int_list)
        max_in_list = max(int_list)
        avg_of_list = sum(int_list) / len(int_list)

        print(f"Input list: {int_list}")
        print(f"Sorted list:  {sorted_list}")
        print(f"Composite list:  {composite_list}")
        print(f"Min: {min_in_list}, Max: {max_in_list}, Average: {avg_of_list:.2f}")

def user_input():
    user_input = input("Enter integers separated with commas: ").split(",")

    int_list = []
    for x in user_input:
        try:
            x = int(x)
            if(x < 0):
                print("Incorrect input!")   
                return [], False
            else:
                int_list.append(x)
        except:
            print("Incorrect input!")
            return [], False

    return int_list, True

def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise, do not change this function'''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
        
if __name__ == "__main__":
    main()
