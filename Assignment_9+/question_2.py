# ...add your function(s) here

def open_file_in_binary(filename):
    try:
        with open(filename, "rb") as file:
            print(b"{file.readlines()}")
    
    except FileNotFoundError:
        print(f"No file named {filename} could be found")

# This line you can keep as is
# file_name = input("Enter file name: ")

# ...and fill in the rest

open_file_in_binary("test1.bin")