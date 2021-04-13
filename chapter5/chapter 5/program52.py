#Victoria Alvarado 2317120
#create main and void function
#use for loop to generate 5 number
#generate 5 random integer each greater than 10 and less than 30
#Calculate sum
#display results

#import random
import random

#define main function
def main (): 
    #call number function
    number()
#define number function
def number():
    #create a sum variable
    sum = 0
    #use for loop with range of 5
    for count in range (5):
        #create num variable and assign random genareted int
        num = random.randint(10,30)
        #calculate sum
        sum += num
        #display the num variable on the same line
        print(f'{num}',end= ' ')
    #display results
    print(f'\nThe total is {sum}')

#call main function
main()