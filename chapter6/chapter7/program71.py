#Victoria Alvarado 2317120
#create a print number function 
#use a for loop to print the number
#create a odd_even number function
#use a loop to find an odd or even number
#display results
#define main function
#import ramdon library
#create empty list and counter variable
#use a while loop to interate 10 numbers
#create number variable and asign random int
# append number to nums list
#increase counter variable
#call  print_numbers function
#sort nums list
#call print_numbers function
#create a start list and assign 5 elements
#display start list variable
#create a finish list and assign the last 3 elements
#display a finish list
#create a finish list and assign the last 3 elements
#use if statement to check main 
#call main function


#create a print number function 

def print_numbers(nums):
    #use a for loop to print the number
    for num in nums:
        print(f'{num}',end= ' ')
    print('\n')
#create a odd_even number function
def odd_even(nums):
    even = 0
    odd = 0
    #use a loop to find an odd or even number
    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    #display results
    print (f'List had {even} evens and {odd} odds','\n')
    print (f'The 3rd element in sorted nums is {nums[2]}','\n')
#import ramdon library
import random
#define main function
def main ():
    nums = []
    counter = 0
    #use a while loop to interate 10 numbers
    while counter < 10:
        #create number variable and asign random int
        number = random.randint(1,50)
        # append number to nums list
        nums.append(number)
        #increase counter variable
        counter += 1  
    #call  print_numbers function
    print_numbers(nums)
    #sort nums list
    nums.sort()
    #call print_numbers function
    print_numbers(nums)
    #create a start list and assign 5 elements
    start = nums[0:5]
    #display start list variable
    print(start,'\n')
    #create a finish list and assign the last 3 elements
    finish = nums[-3:]

    #display a finish list
    print(finish,'\n')
    
    odd_even(nums)

#use if statement to check main 
if __name__ == '__main__':
    #call main function
    main()