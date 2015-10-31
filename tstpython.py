
for num in range(1,10):  
	for num2 in range(1,10):
		X = num * num2 
		print num, "X" ,num2 , "=" , X 



def times(x,y):
	z=x*y
	return z
print times(9,8)

def bigger (x,y):
	if x > y:
		return 1 
	else :
		return 0 
		
def logicAnd(a,b):
	return  a&b
	
def logicOr(a,b):
	return  a|b  
	
print logicOr(1,4)

