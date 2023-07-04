productNames, productCosts = [],[]
VAT = 0.2

while True:
    name = input("Name: ")
    cost = input("Float: ")

    if name.upper() == "NONE" or str(cost).upper() == "NONE":
        print(productNames)
        print(productCosts)
        break

    if not(name.isalpha()):
        print("Name is not valid")
        break

    try:
        cost = float(cost)
    except:
        print("Cost is not valid")
        break

    productNames.append(name)
    productCosts.append(cost)

maxCostIndex = productCosts.index(max(productCosts))
minCostIndex = productCosts.index(min(productCosts))
average = sum(productCosts) / len(productCosts)

for items in range(len(productCosts)):
    if productCosts[items] > 50:
        productCosts[items] = productCosts[items] * 0.95

    totalCost =+ productCosts[items]

totalCost *= (1 + VAT)

print(f"£{round(max(productCosts),2)} - '{productNames[maxCostIndex]}' + 5% off if applicable")
print(f"£{round(min(productCosts),2)} - '{productNames[minCostIndex]}' + 5% off if applicable")
print(f"Average Cost: £{round(average,2)}")
print(f"£{round(totalCost,2)} incl. VAT + 5% off > £50")