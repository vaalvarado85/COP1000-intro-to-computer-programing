HIGH_SCORE = 95
#Get the first test score
first_test_score = float(input('Enter first test score: '))
#Get the second test score
second_test_score = float(input('Enter second test score: '))
#Get the third test score
third_test_score = float(input('Enter third test score: '))
#calculate the average
average_calcualted = (first_test_score + second_test_score + third_test_score)/3
#print the average
print (average_calcualted)
print(f'The average score is {average_calcualted}.')
#if the average is a high score,
#congratulate the user.
if average_calcualted >= HIGH_SCORE:
    print("congratulations!")
    print('that is a great average!')