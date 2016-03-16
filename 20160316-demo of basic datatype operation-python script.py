'''
Numbers
'''
print("5+2",5+2)
print("5-2=",5-2)
print("5*2=",5*2)
print("5%2",5%2)
print("5**2",5**2)

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
print(name[-5]) # count from right, here indcies start from -1
print(name[:7]) # characters from beginning to 7 th position
print(name[5:]) # characters from end to 5 position

'''
Lists
'''
squares = [1,2,4,9,16]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares + [36,49,64,81,100])
squares[2]=121
print(squares)
squares.append(36)
print(squares)
squares.append(7*7)
print(squares)
squares[1:3]=[12,144,135]
print(squares)

