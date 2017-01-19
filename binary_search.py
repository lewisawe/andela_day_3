class BinarySearch(list):
	def __init__(self, a, b):
		self.length = a
		for x in range(1, a+1):
			self.append(x*b)
		
	def search(self, item):
		result = {'count':0, 'index':-1}
		index = [0, (len(self) - 1)]
		half_point = index[1] / 2
		while result['index'] is -1 and index[1] > index[0]:
			if item == self[half_point]:
				result['index'] = half_point
			else:
				if item < self[half_point]:
					index[1] = half_point - 1
				else:
					index[0] = half_point + 1
				half_point = (index[0] + index[1]) / 2
			result['count'] = result['count'] + 1
		return result