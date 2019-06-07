def count_to(count):
	"""Our iterator implementation"""
	
	#Our list
	numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

	#Our built-in iterator
	#Creates a tuple such as (1, "eins")
	iterator = zip(range(count), numbers_in_german)
	
	#Iterate through our iterable list
	#Extract the German numbers
	#Put them in a generator called number
	for position, number in iterator:
		
		#Returns a 'generator' containing numbers in German
		yield position + 1, number 

#Let's test the generator returned by our iterator
for pos, num in count_to(3):
	print("{} is {}".format(num, pos))

for pos, num in count_to(4):
	print("{} is {}".format(num, pos))
	