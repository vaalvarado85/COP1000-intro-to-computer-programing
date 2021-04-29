#This program writes three lines of data 
#to a file
def main():
    print('this was hit')
    #open a file named philosophers
    outfile = open('philosophers.txt','w')
    #to a file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    #close the file.
    outfile.close()
#call the main function.
if __name__ =='__main__':
    main()

    