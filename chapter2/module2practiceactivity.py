#Victoria Alvarado cop1000 
#create variable for test score one and assign user input with displaying prompt to user
#create variable for test score two and assign user input with displaying prompt to user
#create variable for test score three and assign user input with displaying prompt to user
#create variable and assign the average of the three test score
#display average variable with two decimal places and % symbol

#create variable for test 1 and get test score for test 1
test1 = float(input('Enter the score for test 1:'))
#create variable for test 2 and get test score for test 2
test2 = float(input('Enter the score for test 2:'))
#create variable for test 3 and get test score for test 3
test3 = float(input('Enter the score for test 3:'))
#create variable to store average 
average = (test1+test2+test3)/3
#display result to user
print(f"The average of these scores is {average/100:.2%}")