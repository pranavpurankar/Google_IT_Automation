'''
Question 5
Fill in the blanks to complete the “car_listing” function. This function accepts a 
“car_prices” dictionary. It should iterate through the keys (car models) and values
(car prices) in that dictionary. For each item pair, the function should format a 
string so that a dictionary entry like ““Kia Soul“:19000” will print "A Kia Soul 
costs 19000 dollars". Each new string should appear on its own line.
'''

def car_listing(car_prices):
    result = ""
    # Complete the for loop to iterate through the key and value items
    # in the industry
    for models, price in car_prices.items():
        result +=  f"A {models} costs {price} dollars\n"# Use a string method to format the required string
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius": 24000}))
