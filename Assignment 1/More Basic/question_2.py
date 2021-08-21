degrees_f_str = input("Temperature in Fahrenheit: ")
# Convert degrees_f_str to an integer
degrees_c = int(degrees_f_str) 
# Convert to °C
degrees_c = ((degrees_c-32)*5)/9
# Round to nearest whole number
degrees_c = round(degrees_c)
print("That's", degrees_c, "degrees Celcius")