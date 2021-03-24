# to find all count of occurences of all the elements present in a list

from collections import Counter
my_list = [1,2,3,3,3,4,5,5,5,5,5,5,9,0,1] 
a=Counter(my_list)
print(a[4])
