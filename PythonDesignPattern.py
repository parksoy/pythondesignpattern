class Coffee:
    def cost(self):
        return 5  # Base cost of a plain coffee
    
# Base CoffeeDecorator class (Decorator)
class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

# Create a plain coffee
plain_coffee = Coffee()
print("Cost of plain coffee:", plain_coffee.cost())  # Output: Cost of plain coffee: 5

# Add milk to the coffee using a decorator
coffee_with_milk = MilkDecorator(plain_coffee)
print("Cost of coffee with milk:", coffee_with_milk.cost())  # Output: Cost of coffee with milk: 7

# Add sugar to the coffee using a decorator
coffee_with_sugar = SugarDecorator(plain_coffee)
print("Cost of coffee with sugar:", coffee_with_sugar.cost())  # Output: Cost of coffee with sugar: 6

# Add both milk and sugar to the coffee
coffee_with_milk_and_sugar = MilkDecorator(SugarDecorator(plain_coffee))
print("Cost of coffee with milk and sugar:", coffee_with_milk_and_sugar.cost())  # Output: Cost of coffee with milk and sugar: 8
