#Victoria Alvardo cop1000 2317120
#define a main function
#create course variable and prompt the user to enter a course name
#create outfile variable and call open function to get the file
#use a while loop its not equal to empty
#create a percent achieved variable and prompt to the user to enter percentage
#call the write function to save course and percentage
#create sentinel
#close outfile 
#display file created
#if statement to check main name 
#call main function

#define a main function
def main():
    #create course variable and prompt the user to enter a course name  
    course = input('Enter course or Enter to quit :')
    # create outfile variable and call open function to get the file
    outfile = open('grades.txt','w')
    #use a while loop its not equal to empty
    while course != '':
    #create a percent achieved variable and prompt to the user to enter percentage
        percent_achieved = input('Enter percent achieved :')
    #call the write function to save course and percentage    
        outfile.write(f'{course}\n')
        outfile.write(f'{percent_achieved}\n')
    #create sentinel   
        course = input('Enter course or Enter to quit :')
    #close outfile     
    outfile.close()
    #display file created
    print ('File was created and closed')
#if statement to check main name 
if __name__ == '__main__':
    #call main function   
    main()
