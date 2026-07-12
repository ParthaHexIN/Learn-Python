a ={3,25,1}
b = {23,1,2,25,6}
print(a)
print(b)


c= a.union(b) #contains all the elements of both sets without duplicates 
print(c)


d = a.intersection(b)  # contains only the elements which are present in both sets 
print(d)


e = a.difference(b) #contains the elements which are present in a but not in b
print(e)


k = a.symmetric_difference(b) #contains the elements which are present in either a or b but not in both
print(k)
