#Victoria Alvarado 2317120
#create main and cuber functions
#prompt a cube side length
#call cuber function with length as an argument
#Display surface area and volume

#import math
import math

#define main function
def main():
    #create a length variable and assign user float input
    length = float(input('Enter side length of cube'))
    #create area and volume variable,and calling cuber function with length as an argument
    area,volume = cuber(length)
    #display surface area
    print(f'Surface area is {area:.3f}')
    #dislay volume 
    print(f'Volume is {volume:.3f}')

#define cuber function with length as a parameter
def cuber(length):
    #calculate surface area
    surface_area = 6 * math.pow(length,2)
    #calculate volume
    volume = math.pow(length,3)  
    #return results
    return (surface_area,volume)

#call main function
main()

