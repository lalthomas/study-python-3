def sum(n):
	i,total=0,0;
	if n>0:
		while i<=n:
			total+=i
			i+=1
	return total

print(sum(100))
print(sum(200))

