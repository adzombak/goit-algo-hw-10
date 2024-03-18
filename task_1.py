from pulp import LpProblem, LpMaximize, LpVariable

model = LpProblem(name="Maximize production", sense=LpMaximize)

x1 = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
x2 = LpVariable(name="Fruite juice", lowBound=0, cat="Integer")

model += x1 + x2

# Constraints
model += 2 * x1 + x2 <= 100  # Water
model += x1 <= 50  # Sugar
model += x1 <= 30  # Lemon juice
model += 2 * x2 <= 40  # Fruit mash

model.solve()

print(f"Optimal production of Lemonade: {int(x1.value())} units")
print(f"Optimal production of Fruit juice: {int(x2.value())} units")
print(f"Total production: {int(x1.value()) + int(x2.value())} units")
