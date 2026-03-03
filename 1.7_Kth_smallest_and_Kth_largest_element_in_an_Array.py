# FOR KTH LARGEST ELEMENT

def kth_largest_element(array,n,k):
        for j in range(k):
            max=j
            for i in range(j+1,n):
                if (array[i]>array[max]):
                    max=i
            array[j] , array[max] = array[max] , array[j]
        return array[k-1]

array=[21,31,41,51,64,70,-52,-89,-70]
n=len(array)
k=3
res=kth_largest_element(array,n,k)
print(res)

#TIME COMPLEXITY:-  O(n^2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FOR KTH SMALLEST ELEMENT

def kth_smallest_element(array,n,k):
        for j in range(k):
            min=j
            for i in range(j+1,n):
                if (array[i]<array[min]):
                    min=i
            array[j] , array[min] = array[min] , array[j]
        return array[k-1]



array=[21,31,41,51,64,70,-52,-89,-70]
n=len(array)
k=3
res=kth_smallest_element(array,n,k)
print(res)

#TIME COMPLEXITY:-  O(n^2)