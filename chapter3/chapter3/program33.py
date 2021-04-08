#Victoria Alvarado 2317120
#Create constant variables
#Get number of T-shirts desired from user
#Calculate total before taxes
#Use if statement to determine T-shirts price w/o discount
#Calculate shipping fee
#Calculate total price
#display price to the user

#create variable with constant shipping rate, discount and unit price
SHIPPING_RATE = 1.05
DISCOUNT40= .40
DISCOUNT30 = .30
DISCOUNT20 = .20
UNIT_PRICE = 9.99
#Get quantity desired
quantity_desired = int(input('How many T-shirts would you like order?'))
#Determine  T-shirts price with if statement
if quantity_desired >=15:
    total_t_shirts_price = quantity_desired * (UNIT_PRICE * DISCOUNT40)

elif quantity_desired >=10:
    total_t_shirts_price = quantity_desired * (UNIT_PRICE * DISCOUNT30)

elif quantity_desired >= 4:
    total_t_shirts_price = quantity_desired * (UNIT_PRICE * DISCOUNT20)
else:
    total_t_shirts_price = quantity_desired * UNIT_PRICE

total_t_shirts_price = quantity_desired * total_t_shirts_price
#Calculate Shipping cost
shipping_fee = quantity_desired * SHIPPING_RATE
  #calculate total price  
total_price = total_t_shirts_price + shipping_fee
#Display values to user
print (f'Total t-shirts price ${total_t_shirts_price:,.2f}')
print (f'Shipping fee ${shipping_fee:,.2f}')
print (f'Total payable ${total_price:,.2f}')








