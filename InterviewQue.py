#Find the least positive missing num in the list 

A=[1,0,5,2,4,-1,7]

def smallestmissing(A):
    A= set(A)
    smallest=1
    while smallest in A:
        smallest+=1
    return smallest

print(smallestmissing(A))
