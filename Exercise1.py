namesOfPeople = ['John','Andrew','Ssabasi','Joseph','Lubwama']
# Outputting the first item
print(namesOfPeople[1])
# Changing the first item
namesOfPeople[0] = 'Mulondo'
print(namesOfPeople)
# Adding the sixth item
namesOfPeople.append('Aminah')
print(namesOfPeople)
# Adding the third item
namesOfPeople.insert(2, 'Bathel')
print(namesOfPeople)
# Removing the fourth item
del namesOfPeople[3]
print(namesOfPeople)
# Outputting the last item
print(namesOfPeople[-1])
# Printing 3rd, 4th and 5th items from new list
new_list = ["one", "two", "three", "four", "five", "six", "seven"]
print(new_list[2:5])

# Copy list of countries
countries = ["Uganda", "Kenya", "Tanzania"]
countries_copy = countries.copy()
print(countries_copy)

#  for Loop through countries
for country in countries:
    print(country)

# Sortting animal names
animals = ["dog", "cat", "elephant", "ant", "giraffe"]
print(sorted(animals))
print(sorted(animals, reverse=True))

#  Outputting animal names with 'a'
for animal in animals:
    if 'a' in animal:
        print(animal)

# Joining two lists
first_names = ["Mulondo", "Nabukeera"]
last_names = ["Andrew", "Phiona"]
full_names = first_names + last_names
print(full_names)
