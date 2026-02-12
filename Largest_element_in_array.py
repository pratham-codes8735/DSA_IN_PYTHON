Array=[1,2,3,14,5]

largest=Array[0]

for i in Array[1:]:
    if i>largest:
        largest=i
       
print(f"element with maximum value in array is :- {largest}")     

'''
ALTERNATE SOLUTION TO PRINT FINAL STATEMENT:-

print("Element with maximum value in array is :- " + str(largest))

'''
