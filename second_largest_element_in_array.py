Array=[1,2,3,4,5]
first=second=float('-inf')

for i in Array[0:]:
    if i > first:
        second= first
        first=i

    elif i<first and i> second and i!=first:
        second =i
print(f"the first largest and the second largest elements in the given array are {first} and {second} respectively.")        

     