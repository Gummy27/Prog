FIRST_LETTER = 'A'
BOOKED_LETTER = 'X'

def initialize_seating(no_of_rows, no_of_seats):
    ''' Returns an empty seating allocation: list of lists
        Each seat in each row is marked with a letter, starting from "A" '''
    seating = []
    for _ in range(0, no_of_rows):
        seats = []
        # creates consecutive letters starting from first_letter
        for col in range(0, no_of_seats):
            next_letter = chr(ord(FIRST_LETTER) + col)  
            seats.append(next_letter)
        seating.append(seats)
    return seating

def print_out_seating(seating_matrix):
    """
        This function prints out the seating in columns.
    """
    middle = len(seating_matrix[0])/2

    for row_index in range(len(seating_matrix)):
        index_spacing = 2 - len(str(row_index+1))
        print(" "*index_spacing+str(row_index+1), end="   ")
        for seat_index in range(len(seating_matrix[row_index])):
            # This check ensure the middle divide.
            if(seat_index == middle):
                print("  ", end="")
            print(seating_matrix[row_index][seat_index], end=" ")
        print()
    
def convert_seat_number(seat_number):
    """
        This function converts user seat number into cords that can
        be used to index the seating matrix.
    """
    num, letter = seat_number.split(" ")

    num = int(num)-1
    letter = ord(letter.upper())-ord("A")

    return num, letter

def seat_available(seating, matrix_cords):
    """
        This checks if the seat is taken and returns the bool value.
    """
    index1, index2 = matrix_cords

    return (seating[index1][index2] != "X")

def insert_into_seat(seating, matrix_cords):
    """
        This function inserts the person into the seating and returns
        it.
    """
    index1, index2 = matrix_cords

    seating[index1][index2] = "X"

    return seating

def register_seat(seating):
    """
        This function asks the user where he/she wants to sit. It will
        ask the user until a valid input is received.
    """
    while(True):
        seat_number = input("Input seat number (row seat): ")
        try:
            matrix_cords = convert_seat_number(seat_number)
            if(seat_available(seating, matrix_cords)):
                return insert_into_seat(seating, matrix_cords)
            else:
                print("That seat is taken!")
        except(IndexError, ValueError):
            print("Seat number is invalid!")

def any_available_seats(seating):
    for row in seating:
        for seat in row:
            if(seat != "X"):
                return True
    return False

# Main program starts here
def main():
    no_of_rows = int(input("Enter number of rows: "))
    no_of_seats = int(input("Enter number of seats in each row: "))

    seating = initialize_seating(no_of_rows, no_of_seats)

    print_out_seating(seating)

    more_seats = "y"
    while(more_seats == "y"):  
        seating = register_seat(seating)
        print_out_seating(seating)

        if(any_available_seats(seating)):
            more_seats = input("More seats (y/n)? ")
        else:
            more_seats = "n"



if __name__ == "__main__":
    main()