#this program reads and dispalys the contents
#of the philosophers.txt.
def main():
    #open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    #read the file's contents.
    file_contents = infile.read()

    #close the file.
    infile.close()

    #print the data that was read info
    #memory.
    print(file_contents)

#call the main function.
if __name__ == '__main__':
    main()