
# Create set with constructor
beverages = set(("tea", "coffee", "juice"))
print(beverages)

# Add 2 more items
beverages.update(["soda", "milk"])
print(beverages)

# Check if "microwave" is present
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)

# Remove "kettle"
mySet.remove("kettle")
print(mySet)

# Loop through set
for item in mySet:
    print(item)

# Add elements from list to set
my_set = {"a", "b", "c", "d"}
my_list = ["e", "f"]
my_set.update(my_list)
print(my_set)

# Join two sets
ages = {25, 30}
names = {"Alice", "Bob"}
combined = ages.union(names)
print(combined)
