def missing_number(array1, array2):
	array1 = set(array1)
	array2 = set(array2)
	if array1 == array2:
		return 0
		if array1 != array2:
			array3 = list(array2 - array1)
			for value in array3:
				return value
			else:
				False
	