import csv
#import matplotlib.pyplot as plt
#import cowsay


ALL_THE_ANIMALS = ['🐈', '🐕', '🐘', '🐙', '🦓', '🐅']

def hello_world_function():
	# This is a comment
	print('Hello World')

def hello_variable(name = 'Zürich'):
	print('Hello {}'.format(name))
	"""
	This is a multiline
	comment :)
	"""
	print('Hello %s' % name)

def print_animals(animals):
	for index, animal in enumerate(animals, start = 1):
		print('The animal at position {} is a {}'.format(index, animal))

def print_range(start = 0, stop = 10, step = 2):
	for i in range(start, stop, step):
		print(i)


def print_hello():
	hello_world_function()
	hello_variable()
	hello_variable('Tech Face')




class Human:
	def __init__(self, is_female = True):
		self.is_female = is_female

	def greet(self):
		if self.is_female is True:
			print('👩: Hello everybody')
		else:
			print('👨: Hello everybody')

	def greet2(self):
		if self.is_female == True:
			print('👩: Hello everybody')
		else:
			print('👨: Hello everybody')

	def greet3(self):
		if self.is_female:
			print('👩: Hello everybody')
		else:
			print('👨: Hello everybody')


def print_humans():
	woman = Human(is_female = True)
	man = Human(False)
	woman.greet()
	man.greet()






LIST_NUM = [1,2,3,4]
TUP_NUM = (1,2,3,4)

def print_tuples():
	print(LIST_NUM)
	print(TUP_NUM)

def edit_tuples():
	#try:
	LIST_NUM[2] = 5
	print(LIST_NUM)

	TUP_NUM[2] = 5
	print(TUP_NUM)
	#except TypeError as error:
	#	print('Catched TypeError', error)


def why_tuples():
	print('LIST =',LIST_NUM.__sizeof__())
	print('TUPLE =',TUP_NUM.__sizeof__())

	movies = [('Swordfish', 'Dominic Sena', 2001), ('Snowden', ' Oliver Stone', 2016), ('Taxi Driver', 'Martin Scorsese', 1976)]


def divide(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError as e:
		print('Error: Invalid argument: {}'.format(e))
	finally:
		print("-- division finished --")




def deaths_in_zh_per_quartier(year1, year2, year3):
	quarts = [[],[],[]]
	deaths = [[],[],[]]
	with open('deaths.csv', mode='r', encoding='utf-8') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			if int(row['Jahr']) == year1:
				quarts[0].append(row['QuarLang'])
				deaths[0].append(int(row['AnzSterWir']))
			elif int(row['Jahr']) == year2:
				quarts[1].append(row['QuarLang'])
				deaths[1].append(int(row['AnzSterWir']))
			elif int(row['Jahr']) == year3:
				quarts[2].append(row['QuarLang'])
				deaths[2].append(int(row['AnzSterWir']))
	print(quarts, deaths)

	fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
	axs[0].bar(quarts[0], deaths[0])
	axs[1].bar(quarts[1], deaths[1])
	axs[2].bar(quarts[2], deaths[2])
	fig.suptitle('Deaths per Quartier in Zürich')
	axs[0].figure.autofmt_xdate(rotation=90)

	plt.show()


if __name__ == '__main__':
    print_hello()
    #print_range(0, 100, 10)
    #print_animals(ALL_THE_ANIMALS)
    #print_humans()
    #print_tuples()
    #edit_tuples()
    #why_tuples()
    #divide(7)
    #print('Is 🐈 in ALL_THE_ANIMALS? {}'.format('🐈' in ALL_THE_ANIMALS))
    #print('Is 🐄 in ALL_THE_ANIMALS? {}'.format('🐄' in ALL_THE_ANIMALS))

    #deaths_in_zh_per_quartier(1993, 2000, 2019)
    #cowsay.dragon("Hello")
    