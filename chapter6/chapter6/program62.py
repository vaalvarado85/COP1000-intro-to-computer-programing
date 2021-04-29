#Victoria Alvarado 2317120
#create a main function
#creare a infile variable 
#read the first line from the file
#create a counter and total variable 
#create a if and while loop statement 
#display start message
#increasing the counter
#assigned a course with the line variable
#create a score variable and add score from file
#create a total variable and add score to it
#display course and score
#get the next course line
#calculate grade average
#display average 
#display a message for no score
#call the main function


#create a main function
def main():
    #create a variable infile
    infile = open ('grades.txt','r')
    #read the first line from the file
    line = infile.readline()   
    #create a variable counter 
    counter = 0
    #create a variable total
    total = 0
    #create a if statement 
    if line != '':
        #display  start message
        print(f'Here are your grades \n')
    
        #create a while loop
        while line != '':
            #increasing the counter
            counter += 1
            #assigned a course with the line variable
            course = line.rstrip('\n')
            #create a score variable and add score from file
            score = int(infile.readline())
            #create a total variable and add score to it
            total += score
            #display course and score
            print(f'{course} score is {score}\n')
            #get the next course line
            line = infile.readline()
        #calculate grade average
        average = total/counter
        #display average
        print(f'Average grade score is {average:.2f}\n')
    else:
        #display a message for no score
        print(f'No test scores')
#if statement to check main name 
if __name__ == '__main__':
    #call main function
    main()