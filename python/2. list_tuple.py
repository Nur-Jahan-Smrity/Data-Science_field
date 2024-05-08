# Section 1: Python Lists
# -----------------------

# Copy a list(This part is very much important . be careful while doing so .)
duplicate_list = simple_list
duplicate_list.append(7)
print("simple_list id", id(simple_list), "duplicate_list id: ", id(duplicate_list))
print("Duplicate List: ", duplicate_list)
print("Simple List: ", simple_list)
list_copy = simple_list.copy()
list_copy.append(8)
print("List Copy: ", list_copy)
print("Simple List: ", simple_list)

# Assignment 1: Create a 2D list representing a 3x3 matrix and perform operations like accessing, modifying, and iterating through it.

matrix = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
#accessing matrix
print(matrix[1][2])
#modifying the matrix
matrix[1][2] = 60006
print(matrix[1][2])
#iterating elements 
for row in matrix:
    for element in row:
        print(element,end=" ")
    print()

# Section 2: Python Tuples
# ------------------------

# Assignment 2: Create a tuple with mixed data types and demonstrate its potential use cases in data structures like dictionaries.
#tuple with mixed data type
smrity_info =("Smrity",23,"Female",["python","data science"])
another_example_of_key = 10
#dictionary using tuple
my_info = {
    "name": smrity_info[0],
    "age": smrity_info[1],
    "gender": smrity_info[2],
    "my_interest": smrity_info[3]
}
#print the dictionary value 
print(my_info)
#print specific key value of the dictionary 
print("interest : ",my_info["my_interest"])
print("age : ",my_info["age"])


# Section 3: Advanced Applications
# --------------------------------

# Assignment 3: Create a list of tuples, where each tuple contains a student's name and their grade. Sort this list by grades.


# Congratulations on completing the advanced section on Python lists and tuples!
# Review the assignments, try to solve them, and check your understanding of these versatile data structures.
