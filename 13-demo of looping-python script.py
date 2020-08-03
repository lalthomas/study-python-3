'''
while loop
'''''
i=100

while i<5:
	print(i)
'''
for loop
'''
for i in range(5):
	print(i)

words=['india','america','russia']

for w in words:
	print(w,len(w))
	
for w in words[:]:
	words.insert(len(w),'-----')
	
for w in words:
	print(w)



