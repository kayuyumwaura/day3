#function that compares the values in two arrays and returns the missing value
def missing_number(array1, array2):
	array1 = set(array1)
	array2 = set(array2)
	#if none is missing, i.e arrays are similar return zero
	if array1 == array2:
		return 0
		#if arrays are not similar, put missing values in the list
		if array1 != array2:
			array3 = list(array2 - array1)
			for value in array3:
				return value
			else:
				False
	