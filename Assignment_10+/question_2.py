number_of_people = ""
while(isinstance(number_of_people, str)):
    number_of_people = input("Number of people: ")

    try:
        number_of_people = int(number_of_people)
    except:
        print(f"{number_of_people} is not an integer. Please try again.")


people_name = []
people_age = []
for person in range(number_of_people):
    people_name.append(input(f"Name of person {person+1}: "))

    person_age = ""
    while(isinstance(person_age, str)):
        person_age = input(f"Age of person {person+1}: ")

        try:
            person_age = int(person_age)
        except:
            print(f"{person_age} is not an integer. Please try again.")
    people_age.append(person_age)

highest, lowest = 0, 0
for x in range(1, len(people_age)):
    if(people_age[x] < people_age[lowest]):
        lowest = x
    elif(people_age[x] > people_age[lowest]):
        highest = x

print(f"The oldest person is {people_name[highest]} who is {people_age[highest]} years old ")
print(f"The youngest person is {people_name[lowest]} who is {people_age[lowest]} years old")

people_age = sorted(people_age)

median_index = (number_of_people+1)/2
if(median_index % 2 == 0):
    median_age = people_age[int(median_index-1)]
else:
    median_index = round(median_index)
    median_age = (people_age[median_index-1] + people_age[median_index]) / 2

print(f"The median age is {round(median_age, 2)}")
print(f"The average age is {round(sum(people_age)/number_of_people, 2)}")