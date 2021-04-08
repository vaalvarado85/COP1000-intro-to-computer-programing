#Victoria Alvarado 2317120
#create a counter and sum variable 
#Get an integer number from the user
#Use while loop
#Calculate sum
#increase counter variable
#use sentineal to get a new integer
#Calculate average
#Display result

#Create a counter and sum variable
counter = 0
sum = 0

#Get an integer number from user
integer = int(input("Enter integer (enter 0 to end) "))
#Use while loop
while integer != 0:
    #Calculate sum
    sum = sum + integer
    #Increase counter variable
    counter = counter + 1
    #Use sentineal to get a new integer
    integer = int(input("How long? (enter 0 to end) "))
#Calculate average
average = sum/counter  
#Display result  
print(f'The average is {average }')
