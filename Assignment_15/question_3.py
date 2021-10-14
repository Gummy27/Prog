def main():
    chemical_eq_1 = input("Input a chemical equation: ")
    chemical_eq_2 = input("Input another chemical equation: ")

    chemical_eq_set_1 = get_chemical_eq_set_from_string(chemical_eq_1)
    chemical_eq_set_2 = get_chemical_eq_set_from_string(chemical_eq_2)

    # print the intersection here below

    print(', '.join(sorted(set(chemical_eq_set_1.intersection(chemical_eq_set_2)))))

def get_chemical_eq_set_from_string(chemical: str) -> set:
    """
        This function takes in a chemical and seperates its components.
    """
    components = set()
    new_component = None

    for component in chemical:
        if(component.isupper()):
            if(new_component != None):
                components.add(new_component)
            new_component = component
        else:
            if(not component.isnumeric()):
                new_component += component
    components.add(new_component)
    return components

if __name__ == "__main__":
    main()