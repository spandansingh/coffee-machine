import asyncio

class CoffeeMachine:

	outlets_count = None
	total_items_quantity = None

	def __init__(self, outlets_count, total_items_quantity):
		self.outlets_count = outlets_count
		self.total_items_quantity = total_items_quantity

	def refill(self, item_name, quantity):
		if item_name not in self.total_items_quantity:
			print(item_name + " is not present as an ingredient.")
			return
		self.total_items_quantity[item_name] += quantity
		return self.total_items_quantity

	def reduce(self, item_name, quantity):
		if item_name not in self.total_items_quantity:
			print(item_name + " is not present as an ingredient.")
			return
		self.total_items_quantity[item_name] -= quantity

	async def prepare(self, beverage_name, beverage):
		for item in beverage:
			if item not in self.total_items_quantity:
				print(beverage_name + " cannot be prepared because " + item + " is not available.")
				return 

		for item in beverage:
			if beverage[item] > self.total_items_quantity[item]:
				print(beverage_name + " cannot be prepared because item " + item + " is not sufficient.")
				return

		for item in beverage:
			self.total_items_quantity[item] -= beverage[item]

		print(beverage_name + " is prepared.")

	def process(self, beverages):
		loop = asyncio.get_event_loop()
		for beverage_name in beverages:
			loop.run_until_complete(self.prepare(beverage_name, beverages[beverage_name]))
		loop.close() 





