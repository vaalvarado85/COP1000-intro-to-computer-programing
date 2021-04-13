#Victoria Alvarado 2317120
#import temperature convert file
#prompt the user to enter a temperature 
#prompt the user to specify temperature and scale
#validate the user input
#Use a if statement to convert based on user input
#Call function in tempconvert file
#Display converted results


#import temperature convert file
import tempconvert
 
#prompt the user to enter a temperature 
temperature = int(input('Enter the temperature to convert '))
#prompt the user to specify temperature and scale
print('Was that input Celsius or Fahrenheit?')
scale = input('Enter C or F ')
#validate the user input
while scale !='F' and scale != 'f' and scale != 'C' and scale != 'c':
    #ask user to enter valid input
    print('Input was invalid!!!')
    scale = input('Enter C or F ')

#Use a if statement to convert based on user input
if scale =='F' or scale == 'f':
        
    #Call function in tempconvert file
    converted_temp = tempconvert.convert_to_celcius(temperature)
    #Display converted results
    print (f'In Celsius, that is  {converted_temp:,.2f}')
elif scale == 'C' or scale == 'c':
    #Call function in tempconvert file
    converted_temp = tempconvert.convert_to_fahrenheit(temperature)
    #Display converted results
    print (f'In Fahrenheit, that is  {converted_temp:,.2f}')


