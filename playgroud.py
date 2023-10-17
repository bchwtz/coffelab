from beverage import Beverage

bev = Beverage("Espresso")
print(bev.types)

keys = list(Beverage.types.keys())

for key in list(Beverage.types.keys()):
    print(key)