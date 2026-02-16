Array=[10,20,30,40,50,60,70,80,90]

New_Array=[]

for i in range (len(Array)-1,-1,-1):
    New_Array.append(Array[i])

print(New_Array)    


#OR

def reverse_array(Array):
    reverse_array=[]
    n=len(Array)
    for i in range(n-1,-1,-1):
        reverse_array.append(Array[i])
    return reverse_array    

Array=[10,20,30,40,50,60,70,80,90]
new_array=reverse_array(Array)

print(new_array)

def reverse_array(Array):
    n=len(Array)
    for i in range(n//2+1):
        temp=Array[i]
        Array[i]=Array[n-i-1]
        Array[n-i-1]=temp

Array=[10,20,30,40,50,60,70,80,90]    

reverse_array(Array)
print(Array)
''' 
time complexity=O(1)
space complexity=O(1)
'''

# Rotation of an array by d times

def rotated_array_by_d_times(Array,n,d):
    d=d%n
    for i in range(d):
        temp = Array[0] 
        for i in range(n-1):
            Array[i]=Array[i+1]
        Array[n-1]=temp    



Array =[10,20,30,40,50,60,70,80,90]
d=3
n=len(Array)

rotated_array_by_d_times(Array,n,d)

print(Array)
