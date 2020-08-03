def person(name):
	print (name)

def personWithAge(name, age):
	print (name, age)

def personWithFriends(name,*friends):
	print (name)
	for f in friends:
		print("friend : ",f)

def personWithAttibutes(name,**capability):
	print (name)
	for c in capability.keys():
		print(c,":", capability[c])	

def templatePersonWithAge(n):
	return lambda sisterAge:n-sisterAge
		
		
def documentFunction():
	'''
	a documented function 1
	'''
	pass

		
person("Dude")
person(name="Dude")
personWithAge("Dude","12")
personWithAge(name="Dude",age="12")
personWithFriends("Dude", "F1","F2","F3");
personWithAttibutes("Dude", weight="normal", height="tall")

# unpacking arguments

friendFromIndia=["Ram","32"]
personWithAge(*friendFromIndia)
friendFromRussia={"name":"puttin","height":"42", "weight":"69"}
personWithAttibutes(**friendFromRussia)

## lambda expression

sisterAge=templatePersonWithAge(12)
friendElderSisterAge=sisterAge(1);
friendYounderSisterAge=sisterAge(2);
print(friendElderSisterAge, friendYounderSisterAge);

print(documentFunction.__doc__)

