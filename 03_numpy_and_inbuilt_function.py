import numpy as np


"""
num = [1, 2, 3, 4, 5];           # 1D Array or list
arr = np.array(num);           # Convert list to numpy array
print("Original array is: ", arr);
print("Shape of the array is: ", arr.shape);
print("Size of the array is: ", arr.size);
"""

# Nested or 2D Array
num1 = [1, 2, 3, 4, 5];
num2 = [6, 7, 8, 9, 10];
num3 = [11, 12, 13, 14, 15];
arr = np.array([num1, num2, num3]);  # Convert list to numpy
"""
print("Original array is: ", arr);
print("Shape of the array is: ", arr.shape);
print("After reshape : \n",arr.reshape(5,3));
print("Shape of the array is: ", arr.shape);
"""
# access elements with index
"""
print(arr[1]);  # prints num2 
print(arr[2][3])   # prints 14
print(arr[0:,2:])  # prints every elements after the index 2 from the every row 
print(arr[0:2,:])  # prints every elements from row 0-1
print(arr[1,1:4])

arr = np.arange(1,10)  #arrange num from 1-10
arr = np.arange(0,12,step=2)    # gives num in difference of 2
print(arr)                      # prints array from 1 to 9
arr = np.arange(1,15).reshape(3,5)  
print(arr)


arr = np.linspace(1,8,40)     #it gives 40 equally spaced num from 1 - 8
print(arr)  # prints array from 1 to 8 with 40 elements
"""


# copy() function and broadcasting
"""
even = [2, 4, 6, 8, 10];
arr1 = np.array(even)
arr2 = arr1
arr2[3:] = 20    # all the value after index 3 will be replaced by 20
print(arr2)
print(arr1)       #value of arr1 has also changed 



odd = [1, 3, 5, 7, 9];
arr3 = np.array(odd)
arr4 = arr3.copy()  # copy the array
arr4[3:] = 20    # all the value after index 3 will be replaced
print(arr4)       #value of arr4 has changed
print(arr3)       #value of arr3 has not changed


# Broadcasting

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = arr1 + arr2
print(arr3)  # prints array [5, 7, 9]

num = np.array([2, 5, 20, 50, 80, 100, 200, 500, 1000])
print(num>50)       # returns whether true or false
print(num[num>50])   # returns the elements of num which are greater than 50
print(num*2)         #we can perform varios operation like these
"""



# ones() function
x = np.ones(5)   # BY default it is float datatypes
print(x)             # prints array [1., 1., 1., 1.,1.]

y = np.ones(3,dtype=int)
print(y)             # prints array [1, 1, 1]


# random.rand()   it gives random number from 0-1
# random.randint() it gives random number from 0-9
ran = np.random.rand(3)
print(ran)
ran1 = np.random.randint(0,10,4).reshape(2,2) # returns random integers from 0 to 9 and reshaped the returned value
print(ran1)
ran2 = np.random.randn(3,3)
print(ran2)  # returns random numbers from 0 to 1 with mean 0