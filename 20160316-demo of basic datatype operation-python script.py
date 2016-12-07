'''
Numbers
'''
print("5+2",5+2)
print("5-2=",5-2)
print("5*2=",5*2)
print("5%2",5%2)
print("5**2",5**2)  # exponential
print("5//2",5//2)  # floor division
# multiple assignments
a=b=2
print(a,b)

# relational operators

print("5>2",5>2)
print("5<2",5<2)
print("5>=2",5>=2)
print("5<=2",5<=2)
print("5==2",5==2)
print("5!=2",5!=2)


first=1  # 00001
second=2 # 00010
print(first,"&",second,first&second) # bitwise and
print(first,"|",second,first|second) #bitwise or
print(first,"^",second,first^second) #bitwise xor
print("~",first,~first) # negate
print(first,">>","1",first>>1) #right shift
print(first,"<<","1",first<<1) #left shift

print ("10 to base 2 in decimal | int(\'10\',2) : ",int('10',2))
print("int(12.2) : ", int(12.2))
print("char(98):",chr(98))
print("ord('b')",ord('b'))

c = complex("2+2j")
print("c=",c)
print("abs(c):",abs(c))

print("divmod(5,2):",divmod(5,2))

print("isinstance(1,int):",isinstance(1,int))
print("isinstance(1.0,(int,float)",isinstance(1.0,(int,float)))


'''
Strings
'''

print('spam eggs')
print ("spam eggs")
print('c:\name')
print(r"c:\name")
print("""
	new multiline
	multiline printing
""")
print('good'+'boy')
print('good''bye')
name="Indian Union"
print(name[0])
print(name[-5]) # count from right, here indices start from -1
#slicing
print(name[:7]) # characters from beginning to 7th position
print(name[5:]) # characters from end to 5 position

'''
Lists
'''
squares = [1,2,4,9,16]
print("squares : ",squares)
print("squares[0] : ",squares[0])
print("squares[-1] :",squares[-1])
print("squares[1:] :",squares[1:])
print("squares[-3:] :",squares[-3:])
print("squares + [36,49,64,81,100] :",squares + [36,49,64,81,100])
squares[2]=121
print("after squares[2]=121, squares : ",squares )
squares.append(36)
print("after squares.append(36), squares : ",squares)
squares.append(7*7)
print("after squares.append(7*7), squares : ",squares)
squares[1:3]=[12,144,135]
print("after squares[1:3]=[12,144,135] , squares : ",squares)
print("type(squares) : ", type(squares))

