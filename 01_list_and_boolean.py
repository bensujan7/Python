"""my_str = 'sujan';
c = my_str.isalnum();
print(c);

print('Hello');
print(my_str);
print(my_str*3)"""

"""
students = ["sujan", "sagar", "sudip"]
print(students[1])
students.append("bishwas")
print(students)
students.insert(1,"Thor")
print(students)
print(students[2:])
print(students[:2])
print(students[1:3])
students.append(["Tony", "peter"])  # nested the elements inside the lists i.e, both items store in single index
print(students)
print(students[5][0])        # prints element's at index 5 in the list at index 0
print(students[5][0][2])   # prints element's at index 5 in the list at index 0 at index 2


students.extend([2,3,"spider"]) # extend the list with the elements
print(students)                  # i.e, every item will store as different items in the list

"""


# various operations
num = [1, 2, 4, 8,8 ,10,15]
print(sum(num))  # prints the sum of all elements in the list
print(num.pop())
print(num.pop(1))  # removes the element at index 1 and returns it
#um.push("5")
print(num)  # prints the list after pushing the element
print(num.index(4))  # returns the index of the first occurrence of the specified value
print(num.count(8))  # returns the number of occurrences of the specified value
print(num.sort())  # sorts the list in ascending order
print(num)  # prints the list after sorting
print(min(num))
print(max(num))
print(len(num))  