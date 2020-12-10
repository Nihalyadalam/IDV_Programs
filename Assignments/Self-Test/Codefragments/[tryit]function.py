def addFunc(a, b):
	c = a + b
	print(a, " + ", b, " = ", c)
	return c

def thirdNum(*a):
    print("The 3rd nr is ",     #complete the line

x = addFunc(1, 3) 	            # output: 1 + 3 = 4
thirdNum(1, 3, x, 6) 	        # output: The 3rd nr is 4
