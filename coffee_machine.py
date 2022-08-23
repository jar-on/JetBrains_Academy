# a coffee machine with variable inventory, recipes, and different actions
RESTOCK_PROMPT = 'Write how many %s you want to add:\n'
ingredients = [
    ('water', 'ml of water'),
    ('milk', 'ml of milk'),
    ('coffee beans', 'grams of coffee beans'),
    ('disposable cups', 'disposable_cups'),
    ('money', 'of money'),
    ]
# generates the inventory dictionary on basis of the ingredients list
inventory = {key[0]: {'remaining': 0, 'text': key[1]} for key in ingredients}

drinks = [  # water, milk, coffee beans, cups, cost
    (250, 0, 16, 1, -4),  # espresso
    (350, 75, 20, 1, -7),  # latte
    (200, 100, 12, 1, -6),  # cappuccino
]
# generates a list of recipes dictionaries for easy use with the selection system
recipes = {
            str(key+1): {
                        'water': drinks[key][0],
                        'milk': drinks[key][1],
                        'coffee beans': drinks[key][2],
                        'disposable cups': drinks[key][3],
                        'money': drinks[key][4],
                        }
            for key in range(len(drinks))}


class CoffeeMaker:
    def __init__(self, stock, rec=None):
        self.stock = stock
        self.recipes = rec
        self.selected_recipe = None

    def print_report(self):
        print('\nThe coffee machine has:')
        for key in self.stock.keys():
            if key != 'money':
                print(f"{self.stock[key]['remaining']} {self.stock[key]['text']}")
        print(f"${self.stock['money']['remaining']} {self.stock['money']['text']}\n")

    def restock(self, initial_stock):
        if initial_stock:
            self.stock['water']['remaining'] = initial_stock[0]
            self.stock['milk']['remaining'] = initial_stock[1]
            self.stock['coffee beans']['remaining'] = initial_stock[2]
            self.stock['disposable cups']['remaining'] = initial_stock[3]
            self.stock['money']['remaining'] = initial_stock[4]
        else:
            print("")
            for key in self.stock.keys():
                if key != 'money':
                    self.stock[key]['remaining'] += int(input(RESTOCK_PROMPT % (self.stock[key]['text'])))
        print("")

    def beverage_selection(self):
        choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        if choice == 'back':
            return False
        else:
            self.selected_recipe = self.recipes[choice]
            return True

    def remove_ingredients(self):
        for key in self.stock.keys():
            self.stock[key]['remaining'] -= self.selected_recipe[key]

    def take_money(self):
        print(f"I gave you ${self.stock['money']['remaining']}\n")
        self.stock['money']['remaining'] = 0

    def check_ingredients(self):
        for item, value in self.selected_recipe.items():
            if not self.stock[item]['remaining'] > value:
                print(f'Sorry, not enough {item}!\n')
                return False
            print('I have enough resources, making you a coffee!\n')
            return True

    def run(self):
        self.restock([400, 540, 120, 9, 550])
        while True:
            choice = input('Write action (buy, fill, take, remaining, exit):\n')
            if choice == 'fill':
                self.restock(None)
            elif choice == 'buy':
                if not self.beverage_selection():
                    continue
                if not self.check_ingredients():
                    continue
                self.remove_ingredients()
            elif choice == 'remaining':
                self.print_report()
            elif choice == 'take':
                self.take_money()
            elif choice == 'exit':
                break


machine = CoffeeMaker(inventory, rec=recipes)
machine.run()
