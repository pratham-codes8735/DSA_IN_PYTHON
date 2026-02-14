Array=[10,20,30,40,50,60,70,80,90]

#printing of array

print(Array)

#printing length of array
print(len(Array))


#negative indexing
print(Array[-2]) #(element of array from last which starts from -1,-2,-3...)

for i in range(len(Array)):
    print(Array[i]) 
# OR

for ele in Array:
    print(ele)

# time complexity is O(1) for both the methods
#


#slicing of array

sliced_array=Array[0:6:1] #(0 ---> starting index , 6---> lastindex which you want to print + 1 ,  1 --> how much gap you want between any two indexes)
print(sliced_array)

'''
#LIST METHODS:-

-append():- adds an element at the end of the list
-insert():- adds an element at the specified position
-extend():- add two list
-pop():- removes the element at the specified position
-remove():- removes the first item with the specified Value
'''


Array.append(120)
print(Array)

Array.insert(1,34)
print(Array)

Array.extend([45,55,65,75])
print(Array)

Array.pop(1)
print(Array)

Array.remove(50)
print(Array)