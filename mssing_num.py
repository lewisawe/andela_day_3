def find_missing(lst1,lst2):
	if not lst1 and not lst2:
		return 0
		if not set(lst1) ^ set(lst2):
			return 0
		else:
			return list(set(lst1)^ set(lst2))[0]