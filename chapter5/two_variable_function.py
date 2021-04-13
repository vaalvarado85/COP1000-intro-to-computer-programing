#This program demostrates two functions that
#have local variables with the same name.

def main ():
    #Call Texas function.
    texas()
    #Call California function
    california()

#definition of the texas function. It creates
#a local variable named birds.
def texas ():
        birds = 5000
        print (f'Texas has {birds} birds.')

#definition of the California function. It also creates
#a local variable named birds.
def california ():
        birds = 8000
        print (f'california has {birds} birds.')
#Call the main function.
main()

