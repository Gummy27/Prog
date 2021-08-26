a = bool(int(input("A")))
b = bool(int(input("B")))
c = bool(int(input("C")))

# compute d
d = (a and not b) or (not a and c)


print("D is", int(d))