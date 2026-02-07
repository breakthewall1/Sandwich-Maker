### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if self.machine_resources[ingredient] >= amount:
                continue
            else:
                print(f"Sorry, there's not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = int(input("How many dollars?: "))
        half = int(input("How many half-dollars?: "))
        quarter = int(input("How many quarters?: "))
        nickel = int(input("How many nickels?: "))
        return dollars + half * 0.5 + quarter * 0.25 + nickel * 0.05

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            return True
        else:
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, amount in self.machine_resources.items():
            self.machine_resources[ingredient] = amount - order_ingredients[ingredient]


### Make an instance of SandwichMachine class and write the rest of the codes ###
maker = SandwichMachine(resources)
while True:
    choice = input("What would you like? (small/medium/large/off/report): ")
    match choice.lower():
        case "off":
            exit()
        case "report":
            print(f'Bread: {maker.machine_resources["bread"]} slice(s)\n'
                  f'Ham: {maker.machine_resources["ham"]} slice(s)\n'
                  f'Cheese: {maker.machine_resources["cheese"]} ounce(s)')
            continue
    ingredients = recipes[choice]["ingredients"]
    cost = recipes[choice]["cost"]
    if not maker.check_resources(ingredients):
        continue
    print("Please insert coins.")
    amount = maker.process_coins()
    if maker.transaction_result(amount, cost):
        print(f'Here is ${amount - cost} in change.')
    else:
        print("Sorry, that's not enough money. Money refunded")
        continue
    maker.make_sandwich(choice, ingredients)
    print(f'{choice} sandwich is ready. Bon appetit!')
