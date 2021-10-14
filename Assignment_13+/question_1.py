from math import tan

def get_function_info(func):
    result_string = f"Name: {func.__name__}"
    result_string += "\n----------------------------------------"
    result_string += f"\n{func.__doc__}"

    return result_string

print(get_function_info(tan))

print("Name: tan\n----------------------------------------\nReturn the tangent of x (measured in radians).")