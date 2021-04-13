#victoria Alvarado cop 1000
#create a program using import random
#create a main function
#Get two randow integer from user
#Display the result

#use import random
import random

#use main function
def main():
    random_num_1 = random.randint(1,5)
    random_num_2 = random.randint(1,5)
    show_larger(random_num_1,random_num_2)

def show_larger(int1,int2):
    if int1 > int2:
        print (f'{int1} is larger than {int2} by {int1-int2}')
    elif int2 > int1:
        print  (f'{int2} is larger than {int1} by {int2-int1}')   
    else:
        print(f'The integers are equal, both are {int1}')
#display results
main()

