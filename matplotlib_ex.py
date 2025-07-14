import matplotlib.pyplot as plt

import numpy as np

# simple example
x=np.arange(0,7)
y=np.arange(8,15)
Y=y*y*y

## plt.scatter ------>

# plt.scatter(x,y,c='b')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('2D garph')
# plt.savefig('2D_graph.png')
# plt.show()

## plt.plot --------->
# plt.plot(x,Y,'g--')   # g is color and -- make smooth line to dotted
# plt.plot(x,Y,'b*-')    # different styles of line
#plt.plot(x,Y,'ro') 
#plt.plot(x,Y,'ro--')
# plt.plot(x,Y,'g*', linestyle='dashed', linewidth= 3, markersize=16 )  
# plt.show()

## creating sub plot --------->
# plt.subplot(2,3,1)    # position of figure 
# plt.plot(x,Y,'b--')
# plt.subplot(2,2,2)
# plt.plot(x,Y,'g*-')
# plt.subplot(2,2,3)
# plt.plot(x,Y,'ro--')
# plt.show()


# x = np.arange(0,7)
# y = x*x-3                 # we can perform  various complex like this
# plt.title('matplotlib demo')
# plt.plot(x,y,'g')
# plt.show()





# # compute x and y for points on sine curve ------->
# x = np.arange(0,4*np.pi,0.2)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()

# sub plot of sine and cosine curve ------->
# x= np.arange(0,5*np.pi,0.2)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# # for sin
# plt.subplot(2,3,1)
# plt.title('sine curve')
# plt.plot(x,y_sin,'b')

# # for cos
# plt.subplot(2,2,2)
# plt.title('cosine curve')
# plt.plot(x,y_cos,'g--')
# plt.show()





# Bar plot ............

# x1 = [1,4,7,10]
# y1 = [10,9,16,12]
# x2 = [2,5,8,11]
# y2 = [8,15,13,10]

# plt.bar(x2,y2)
# plt.bar(x1,y1,color='g')
# plt.title('Bar Graph')
# plt.show()


# Histogram ....................

# a = np.array([2,13,24,45,15,7,3,33,57,72,66,88,68])
# plt.hist(a)
# plt.title("Histogram")
# plt.show()




# pie chart ...........

label = 'c','c++','python','java'
size = [200, 120, 300, 250]
color = ['green', 'blue', 'yellow', 'red']
explode = (0.2, 0.1, 0, 0)

plt.pie(size, explode=explode, labels=label, colors = color,autopct = '%1.1f%%',shadow= True)

plt.axis('equal')
plt.show()