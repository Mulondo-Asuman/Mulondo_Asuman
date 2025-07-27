
x = ("samsung", "iphone", "tecno", "redmi")

#  Output favorite phone brand
print(x[0])

# Negative indexing (2nd last)
print(x[-2])

# Update "iphone" to "itel" (convert to list and back)
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(x)

# Add "Huawei"
x_list.append("Huawei")
x = tuple(x_list)
print(x)

# Loop through tuple
for phone in x:
    print(phone)

# Remove first item
x = tuple(x_list[1:])
print(x)

# Create tuple using constructor
cities = tuple(("Kampala", "Entebbe", "Jinja", "Gulu"))
print(cities)

#  Unpack tuple
city1, city2, city3, city4 = cities
print(city1, city2, city3, city4)

#  Range of cities
print(cities[1:4])

# Join two tuples
first_names = ("Alice", "Bob")
last_names = ("Smith", "Johnson")
full_names = first_names + last_names
print(full_names)

#  Multiply tuple
colors = ("red", "green")
print(colors * 3)

# Count how many times 8 appears
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))