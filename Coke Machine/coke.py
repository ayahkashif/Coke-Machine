#25 10 5
#Insert Coin:
#Amount Due:
#Change Owed:

price = 50
print("Amount Due: " + str(price))

while True:
    insert = int(input("Insert Coin: "))
    if insert not in [5, 10, 25]:
        print("Amount Due: " + str(price))
    elif insert >= price:
        break
    else:
        price -= insert
        print("Amount Due: " + str(price))

print("Change Owed: " + str(insert-price))
