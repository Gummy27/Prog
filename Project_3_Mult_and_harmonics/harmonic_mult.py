from math import floor

harmonic_or_multiplication = input("(h)armonic, (m)ultiplication or (q)uit: ")
while(harmonic_or_multiplication != "q"):
    if(harmonic_or_multiplication == "h"):
        '''
        The harmonic series is simply 1 over the n.

        The algorithm will simply use one variable that will store the sum. The main
        algorithm takes place in a for loop that runs x many times. In the for loop the
        harmonic number is generated using the formula 1/x. This number is then added to 
        the harmonic series.
        '''

        harmonic_sum = 0
        harmonic_length = int(input("Series length: "))

        for x in range(harmonic_length):
            harmonic_sum += 1/(x+1)
            print(round(1/(x+1), 4))
        print("Sum of series:", round(harmonic_sum, 4))

    elif(harmonic_or_multiplication == "m"):
        '''
        The ancient Egyptian method of multiplying is simply that we continually 
        double the other int while halving the other one. When the halved int is
        odd the corresponding doubled int is added to a result variable. This multiplication
        is complete when the halved int reaches 1.

        The program will simply have 3 variables. One to store the sum, another one to 
        store the first int and a third one to store the second int.
            The iteration will happen in a while loop that will stop when the second int reaches
        1. In each iteration the second int is checked if it's odd. If so the first int is
        added to the result variable. 
            Lastly the first int is doubled and the second int is halved. 
            
        '''

        result = 0
        first_int = int(input("First integer: "))
        second_int = int(input("Second integer: "))

        while(second_int > 1):
            print(first_int, second_int)
            if(second_int % 2 != 0):
                result += first_int

            first_int = floor(first_int*2)
            second_int = floor(second_int/2)
        
        print(first_int, second_int)
        result += first_int
        print("Product:", result)

    else:
        print("Illegal choice!")

    harmonic_or_multiplication = input("(h)armonic, (m)ultiplication or (q)uit: ")