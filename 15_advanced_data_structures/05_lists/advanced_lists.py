# create a list
num_list = [1, 2, 3]
print("Create a list with 1, 2, 3 values:", num_list)

# append three 6 to end of list
num_list.append(6)
num_list.append(6)
num_list.append(6)
print("After appending three 6 to end of list:", num_list)

# count a values in list
counter = num_list.count(6)
print("How many 6 in lists:", counter)

# insert a value in a index
num_list.insert(2, "Dimah")
print("After inserting Dimah to index 2:", num_list)

# pop a value with index
poper = num_list.pop(5)
print("Value in index 5 was deleted:", num_list)
print("But we have that in a variable:", poper)

# remove a value with value name
num_list.remove("Dimah")
print("After remove `dimah` from list:", num_list)
