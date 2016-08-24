import numpy
ones=numpy.ones((2,2))
print("ones")
print(ones)
second=ones.copy()
second[0,0]=9
print("ones")
print(ones)
print("seconds")
print(second)
