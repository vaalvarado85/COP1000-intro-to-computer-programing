#Victoria Alvarado 2317120
#Create a variable to get a number from user
#Use nested loop to generate a triangle
#Use the if statement to print o if r<c


#Create a variable to get a number from user
start = int(input("How many lines?"))
#Use nested loop to generate a triangle
for r in range(0,start+1):
    for c in range(0,start+1):
        #Use if statement ro print o if r<c
        if r < c:
           print("o", end= "")
        else:
            print(end= " ")
    print()
