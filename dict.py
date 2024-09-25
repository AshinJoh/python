fruits = {
    "apple": 10,
    "banana": 20,
    "cherry": 15
}

print(fruits["apple"])
fruits["orange"] = 25

del fruits["banana"]

for fruit, quantity in fruits.items():
    print(f"{fruit}: {quantity}")

print(fruits.keys())
print(fruits.values())