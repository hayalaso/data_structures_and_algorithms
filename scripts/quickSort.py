def quickSort(array):
    N = len(array)
    ipiv = N-1
    pivot = array[ipiv]

    j=0
    while j<ipiv:
        if pivot <= array[j]:
            array[ipiv] = array[j]
            array[j] = array[ipiv-1]
            ipiv = ipiv-1
            array[ipiv] = pivot
        else:
            j+=1

    #Now some recursion
    a=[]
    b=[]
    if ipiv==0: #array is either size 1 or 2
           return array
    if ipiv>0 and ipiv<N:
        if ipiv == N-1:
            a=quickSort(array[:ipiv]) 
        else:
            a=quickSort(array[:ipiv])
            b=quickSort(array[ipiv+1:])

    a.append(array[ipiv]) # add our initial pivot back
    return a+b

test = [21,4,1,9,2,3,15,24,29,5,6]
print(test,len(test))
print(quickSort(test),len(quickSort(test)))
