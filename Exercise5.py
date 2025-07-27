
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

#  Print shoe size
print(Shoes["size"])

#  Change brand to Adidas
Shoes["brand"] = "Adidas"
print(Shoes)

# Add key/value pair
Shoes["type"] = "sneakers"
print(Shoes)

# Return all keys
print(Shoes.keys())

# Return all values
print(Shoes.values())

# Check if key exists
print("size" in Shoes)

# Loop through dictionary
for key, value in Shoes.items():
    print(key, ":", value)

# Remove "color"
Shoes.pop("color")
print(Shoes)

# Empty dictionary
Shoes.clear()
print(Shoes)

# 10. Make copy of dictionary
my_dict = {"name": "Alex", "age": 28}
copy_dict = my_dict.copy()
print(copy_dict)

# Nested dictionary
nested_dict = {
    "student1": {"name": "John", "age": 20, "gender": "male"},
    "student2": {"name": "Jane", "age": 22, "gender": "female"}
}
print(nested_dict)
