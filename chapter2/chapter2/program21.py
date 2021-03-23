#Victoria Alvarado cop1000 
#prompt uses for weight in pounds
#convert weight from pounds to kilograms 
#display weight in kilograms

#get weight in pounds from user
weight_pounds = float(input("Enter weight in pounds:"))
#convert weight to kilograms 
converted_weight_kg =weight_pounds/2.2046
#display converted weight
print(f'Your converted weight of {weight_pounds:.1f} pounds to kilograms is {converted_weight_kg:.1f}')