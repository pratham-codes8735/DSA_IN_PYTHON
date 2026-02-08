from math import *

#METHOD_1

def count_digits(num):
    count=0
    while num>0:
    
     r=num%10
    
     num=num//10
     count=count+1
    return count


#METHOD_2
def count_digits(num):
    return int(log10(num)) + 1

num = 5873
print(count_digits(num))
