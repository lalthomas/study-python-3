'''
python data structures 
'''

# List

list = []
list=['apple','orange']
print("list:",list)
print("first element:",list[0])
food_animal=[['apple','orange'],['crow','parot']]
print(food_animal)
print(food_animal[0][0])
even=[2,4,6,8,10]
odd=[1,3,5,7]
numbers=even+odd
print(numbers)
# check for an item in a list
print("Is 0 present in list of ",numbers,0 in numbers)
print("Min of even",min(even))
print("Max of even",max(even))

even.append(12)
print("even : " ,even)
print("even.count(2) : ",  even.count(2))
print("even.index(2) : ", even.index(2))

even.insert(2,'lal')
print("even after insert : " ,even)

list2=[1,23,34,[12,23],'Python']
print("list2 : ",list2)

# last element
list2.pop()
print("list2 after pop : ",list2)

list2.remove(1)
print("list2 after removing list2[1] element : ",list2)

list2.reverse()
print("list2 after reversing",list2)

list.sort()
print("list after sort",list)

list.sort(reverse=True)
print("list after reverse sort",list)

# copying
# assignment will generate 

list3 = list


# Tuples elements can not be changes

tuple1=12,
print("tuple1 : ",tuple1)
print("2*(12,)",2*(12,))
print("5*(12,)",5*(12,))

tuplefromArray= tuple([1,2,3]);
print("tuplefromArray :",tuplefromArray)
tuplefromString=tuple("String");
print("tuplefromString:",tuplefromString)

# Tuple slicing

print("tuplefromArray",tuplefromArray[1])
print("tuplefromArray",tuplefromArray[2:3])

(a,b,c) = ('alpha','beta','gamma')

print(a,b,c)

d = tuple('lal thomas')
print("d :",d)
print("d.count('a') : ",d.count('a'))
print("d.index('l') : ",d.index('l'))



# Sets

set1 = set([1,2,3])
print("set1 :", set1)

set2 = set([1,3,3,4,4])
print("set2 :",set2)

print("set1.union(set2):",set1.union(set2))

set1.add(5)
print("after set1.add(5) : ",set1)

print("set1.intersection(set2) : ",set1.intersection(set2))
print("set1.difference(set2) : ",set1.difference(set2))

