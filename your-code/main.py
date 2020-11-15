#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))
a1 = np.random.randint(1,100, size=(2,3,5))
a2 = np.arange(30).reshape(2,3,5)
a3 = np.empty((2,3,5))

#4. Print a.

print('\n Array a: \n\n', a, '\n')
print('\n Array a1: \n\n', a1, '\n')
print('\n Array a2: \n\n', a2, '\n')
print('\n Array a3: \n\n', a3, '\n')

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.

print('\n Array b: \n\n', b, '\n')

#7. Do a and b have the same size? How do you prove that in Python code?

if a.size == b.size:
    print('Both Arrays a & b have the same size of %s' % b.size, '\n')

#8. Are you able to add a and b? Why or why not?

"It is not possible to add a and b through numpy.add() method as both have different\
shapes (a = 2x3x5 & b = 5,2,3), and  arrays'operations can only be done if both arrays have the\
same structure ..."

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.reshape((2,3,5)) # transpose method returned c.shape = (3,2,5)
print('\n Array c: \n\n', c, '\n')
print("Transposed Array's Structure:",c.shape, '\n')

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)
print('\n Array d: \n\n', d, '\n')

"Now the adding operation is working since both have the same structure or 'shape'\
which can be defined as 2 groups containing three lists of 5 elements each."

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print('\n Array a: \n\n', a, '\n')
print('\n Array d: \n\n', d, '\n')

"Both of the arrays have the same shape or structure of (2,3,5), which also means they have\
the same size of 30 elements. In terms of values the difference relies in a value of 1, as\
all of the elements within Array d are the result of adding 1 to each of the values found in\
Array a, which was the operation done with numpy.add method."

#12. Multiply a and c. Assign the result to e.

e = np.multiply(a,c)
print('\n Array e: \n\n', e, '\n')

#13. Does e equal to a? Why or why not?

"Yes, arrays e and a are equal because all the elements within e are the result of multiplying\
each element of a by 1 ..."

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()
print('The max value in d is ...',d_max,'\n')
print('The min value in d is ...',d_min,'\n')
print('The mean in d is ...',d_mean, '\n')

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))
print('Array (empty) f: \n\n', f, '\n')

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

    # this function is effective, but the problem with it is that it modifies the original array.
def evaluate(array, maxi, mini, mean):
    for a in range(len(array)):
        for lst in range(len(array[a])):
            for x in range(len(array[a][lst])):                
                if array[a][lst][x] == mini:
                    array[a][lst][x] = 0
                elif array[a][lst][x] > mini and array[a][lst][x] < mean:
                    array[a][lst][x] = 25
                elif array[a][lst][x] == mean:
                    array[a][lst][x] = 50
                elif array[a][lst][x] > mean and array[a][lst][x] < maxi:
                    array[a][lst][x] = 75
                elif array[a][lst][x] == maxi:
                    array[a][lst][x] = 100
                else:
                    array[a][lst][x] = '?'
    return array

    # this version is an alternative by converting the array into a list
    # also this version is better as it doesnt create changes on the original array
def evaluate2(array, maxi, mini, mean):
    new_array = []
    for a in array.flatten(): # array.flatten().tolist() # list(array.flatten())
        if a == mini: # we can have the same approach of using indexes like the past function but it would only make it more complicated
            new_array.append(0)
        elif a > mini and a < mean:
            new_array.append(25)
        elif a == mean:
            new_array.append(50)
        elif a > mean and a < maxi:
            new_array.append(75)
        elif a == maxi:
            new_array.append(100)
        else:
            new_array.append('?')
    return np.reshape(new_array, (2,3,5)) 

f = evaluate2(d, d_max, d_min, d_mean)

"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

"Note: By using function evaluate(), the data of d is overwritten, so d and f are the exact same.\
To avoid this situation, I decided to rather employ function evaluate2(), which creates a new array\
from scratch."

print('Array d:\n\n', d)
print('\nNumber of Elements in d:', len(d.flatten()), 'elements.\n')

print('The max value in d is ...',d_max)
print('The min value in d is ...',d_min)
print('The mean in d is ...',d_mean)

print('\nNew Array f:\n\n', f)
print('\nNumber of Elements in f:', len(f.flatten()), 'elements.')

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

bonus = map(lambda x: 'A' if x==0 else('B' if x==25 \
    else('C' if x==50 else('D' if x==75 else('E' if x==100 else '?')))), f.flatten())
# FYI: this map and lambda function isnt practical but for me it seemed more practical for this question.
bonus_f = np.reshape(list(bonus), (2,3,5))

print('\nBonus Array f:\n\n', bonus_f)
print('\nNumber of Elements in Bonus Array f:', len(bonus_f.flatten()), 'elements.')