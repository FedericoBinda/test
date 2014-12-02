def function_sum(a,b):
	return a+b

def function_subtract(a,b):
	return a-b
	
def function_multiply(a,b):
	return a*b
	
def some_crazy_idea(craziness):
	"""Function that spreads craziness!"""
	for i in range(craziness):
		print "I am crazy!", i
	return craziness

def test_function_sum():
	assert(function_sum(1,2) == 3)
	assert(function_sum(1.,2.) == 3.)
	assert(function_sum(2,2) == 4)
	
def test_function_subtract():
	assert(function_subtract(1,1) == 0)
	assert(function_subtract(2,5) == -3)

def test_function_multiply():
	assert(function_multiply(3,2) == 6)
	assert(function_multiply(2,0) == 0)

	
def test_some_crazy_idea():
	assert(some_crazy_idea(2) == 2)