# Итератор
class FlatIterator:
	def __init__(self, data_list):
		self.list = data_list

	def __iter__(self):
		self.cursor = -1

		def flatlist(data):

			lst = []
			for values in data:
				if type(values) == list:
					lst.extend(flatlist(values))
				else:
					lst.append(values)

			return lst

		self.flat_list = flatlist(self.list)

		return self

	def __next__(self):
		self.cursor += 1
		if self.cursor == len(self.flat_list):
			raise StopIteration

		return self.flat_list[self.cursor]

# Генератор
def flatgenerator(income_list):
	lst = []
	def _flat(data):
		for value in data:
			if type(value) != list:
				lst.append(value)
			else:
				_flat(value)
	_flat(income_list)
	for value in lst:
		yield value

if __name__ == "__main__":

# Список с неопределенной вложенностью для проверки:
	nested_list = [
		['a', ['g','b',['ssss']], 'c'],
		['d', 'e', 'f', 'h', False],
		[1, 2, None],
	]

# Список с одноуровневой вложенность для проверки:
	nested_list = [
		['a', 'b', 'c'],
		['d', 'e', 'f'],
		[1, 2, None],
	]

# Запуск итератора
	for item in FlatIterator(nested_list):
		print(item)

	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)

# Запуск генератора
	for el in flatgenerator(nested_list):
		print(el)