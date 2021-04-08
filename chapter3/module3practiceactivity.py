#Victoria Alvarado COP1000
#create a variable with constant tax rate of 7%
#create variable with constant shipping rate at $1
#Get number of pound desired from user
#Use if statement to determine coffee price
#calculate total before taxes
#use if statement to determine shipping cost
#calculate tax fee
#calculate total price
#display price to the user

TAX_RATE = .07
SHIPPING_RATE = 1
pound_desired = int(input('How many pounds are you ordering? '))
if pound_desired >= 40:
    coffee_price = 7.50

elif pound_desired >= 20:
    coffee_price = 8.75

elif pound_desired >= 10:
    coffee_price = 10
elif pound_desired >= 1 and pound_desired <= 9:
    coffee_price = 12

price_of_coffee = pound_desired * coffee_price

if price_of_coffee > 150:
   shipping_cost = 0
else:
    shipping_cost = pound_desired * 1

tax_fee = price_of_coffee * TAX_RATE
total_price = shipping_cost + price_of_coffee + tax_fee
print (f'Cost of coffee ${price_of_coffee:,.2f}')
print (f'{TAX_RATE*100:.0f}% sales tax ${tax_fee:,.2f}')
print (f'Shipping fee ${shipping_cost:,.2f}')
print (f'Total payable ${total_price:,.2f}')







