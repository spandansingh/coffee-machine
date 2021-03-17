import requests

from CoffeeMachine import CoffeeMachine

if __name__ == '__main__':

	r = requests.get(url='https://api.npoint.io/e8cd5a9bbd1331de326a')
	input_json = r.json()["machine"]

	machine = CoffeeMachine(input_json["outlets"]["count_n"], input_json["total_items_quantity"])

	machine.process(input_json["beverages"])