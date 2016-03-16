'''
program to check whether array contain even number
'''

__author__ = 'Lal Thomas'

list=[1,23,34,23,341,23,34,213,213]

for i in range(len(list)):
    if(list[i]%2 ==0 ):
        print ("list contains even number")
        break
else:
    print ("list doesnt contains even number ")

