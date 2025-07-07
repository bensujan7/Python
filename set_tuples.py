# sets
"""
set_var = {"spiderman", "batman", "superman"}
print(set_var);
print(type(set_var));

set_var.add("Hulk");  # use inbuilt function add() to add an element in set
print(set_var);

set1 = {"apple", "banana", "cherry"};
set2 = {"banana", "cherry", "date"};
# use inbuilt function union() to get the union of two sets
print(set1.union(set2));

print(set2.difference(set1));  # perform set2 - set1
print(set2);
print(set1.intersection(set2));  # perform set1 & set2
print(set2.difference_update(set1)); # perform set2 - set1 and update set2

print(set2);
"""



# Dictionary
# dictionary in python is like an object in oop  and it is mutable , it is an unordered collection of key-value pairs
"""
dic = {};             # declare a dictionary  we shouldn't keep items like in set

dic["name"]="John";    # declare a key-value pair
dic["age"]=20;
print(dic);

# Another way of declaring a dictionary is using the dict() function

std = dict(name="John", age=20);
print(std);


# Accessing dictionary elements
# we can access the elements of a dictionary using the key
print(dic["name"]);  # access the value of the key "name"
print(dic.get("age"));  # access the value of the key "age" using the get



#another way
fruits = {"apple": 1, "banana": 2, "cherry": 3};
print(fruits);
print(fruits["apple"])

# we can even loop throughout the key and values of dictionary
for x in fruits: #for keys
    print(x);

for x in fruits.values():
    print(x);

for x in fruits.items():
    print(x);

fruits["mango"]=4;   # add a new key-value pair
print(fruits);

fruits["mango"]=5;    # replace value of the key
print(fruits);


# Nested dictionary
# we can have a dictionary inside another dictionary

sub1_marks = {"math":90}
sub2_marks = {"science":80}
sub3_marks = {"english":70}

result = {"sub1":sub1_marks, "sub2":sub2_marks, "sub3":sub3_marks}
print(result)

print(result['sub1'])    # print the value of the key sub1 i.e, sub1_marks
print(result['sub1']['math'])  # print the value of the key math i.e, 90
print(result["sub2"]["science"])

"""

# Tuples
# Tuples are similar to lists but are immutable i.e, cannot be changed after creation
# Tuples are defined by values separated by comma and enclosed in parentheses ()

tuple = ("Ram", "Shyam", "Hari");
print(tuple);
print(type(tuple))
print(tuple[1])          # accessing the value of the index 1 i.e, Shyam

print(tuple[0:2])        # accessing the values of the index 0 to 1
print(tuple[1:])          # accessing the values of the index 1 to the end


tuple = ("tony", "steve", "bruce");   # tuples can have duplicate values 
print(tuple)                           # single item cannot be changed but whole tuple can be changed
print(tuple.index("steve"))








