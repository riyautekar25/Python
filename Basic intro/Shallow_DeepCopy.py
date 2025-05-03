# A shallow copy creates a new object but still references the same underlying data (nested objects or arrays) as the original. 
# A deep copy, on the other hand, creates a completely independent copy of the object and all its nested elements, ensuring no shared references

#Shallow copy
import copy
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)

original_list[0][0] = 100
print(original_list)        # Output: [[100, 2, 3], [4, 5, 6]]
print(shallow_copied_list)  # Output: [[100, 2, 3], [4, 5, 6]]

#Deep copy
original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)

original_list[0][0] = 100
print(original_list)     # Output: [[100, 2, 3], [4, 5, 6]]
print(deep_copied_list) # Output: [[1, 2, 3], [4, 5, 6]]