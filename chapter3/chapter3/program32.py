#Victoria Alvarado 2317120
#create constant variable
#prompt user for question one answer
#prompt user for question two answer
#check question one and provide feedback
#check question two and provide feedback

#create constant variables
ANSWER1 = 'Earth'
ANSWER2 = 8
#Get answers from user
question_one_answer = input('What is the third planet from de sun?')
question_two_answer = int(input('How many planet are in our solar system?'))
#check answer for question one and provide feedback
if ANSWER1 == question_one_answer:
    print(f'{question_one_answer} is correct!')
else:
    print (f'{question_one_answer} is incorrect!')
#check answer for question two and provide feedback
if ANSWER2 == question_two_answer:
    print (f'{question_two_answer} is correct!')    
else:
    print (f'{question_two_answer} is incorrect')