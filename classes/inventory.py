# from  http://codereview.stackexchange.com/questions/57438/game-inventory-system

class Item(object):
	"""docstring for Item"""
	def __init__(self, name,attack,defence,weight,price):
		self.name = name
		self.attack = attack
		self.defence = defence
		self.weight = weight
		self.price = price


class Inventory(object):
	"""docstring for Inventory"""
	def __init__(self):
		self.items = {}

	def add_item(self,item):
		self.items[item.name] = item

	def tot_price(self):
		tot = 0
		for item in self.items.values():
			tot  = tot + int(item.price)
		print "total price -> ",tot

	def print_items(self):
		print('\t'.join(['Name', 'Atk', 'Def', 'Lb', 'Val']))
		for item in self.items.values():
			 print('\t'.join([str(x) for x in [item.name,item.attack,item.defence,item.weight,item.weight,item.price]]))


inventory = Inventory()
inventory.add_item(Item('Sword', 5, 1, 15, 2))
inventory.add_item(Item('Armor', 0, 10, 25, 5))
inventory.print_items()
inventory.tot_price()
