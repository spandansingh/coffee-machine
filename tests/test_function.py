import unittest 

import sys 
sys.path.append('..')

from CoffeeMachine import CoffeeMachine

class TestSimple(unittest.TestCase): 

	def testRefill(self):

		r = requests.get(url='https://api.npoint.io/e8cd5a9bbd1331de326a')
		input_json = r.json()["machine"]

		machine = CoffeeMachine(input_json["outlets"]["count_n"], input_json["total_items_quantity"]) 

		first_item = list(machine.total_items_quantity.keys())[0]
		first_value = machine.total_items_quantity[first_item]

		machine.refill(first_item,100)

		self.assertEqual(first_value+100, machine.total_items_quantity[first_item])

	def testReduce(self):
		
		r = requests.get(url='https://api.npoint.io/e8cd5a9bbd1331de326a')
		input_json = r.json()["machine"]

		machine = CoffeeMachine(input_json["outlets"]["count_n"], input_json["total_items_quantity"]) 

		first_item = list(machine.total_items_quantity.keys())[0]
		first_value = machine.total_items_quantity[first_item]

		machine.reduce(first_item, 100)

		self.assertEqual(first_value - 100, machine.total_items_quantity[first_item])

if __name__ == '__main__': 
	unittest.main()