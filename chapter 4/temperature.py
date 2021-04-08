#This program assist a technician in the process
#of checking a substances temperature
#named constant to represent the maximun temperature.

MAX_TEMP = 102.5
#Get the substance temperature
temperature = float(input('Enter the substance celsius temperature:'))

# As long as necessary, instruct the user to adjust the thermostat.
while temperature >MAX_TEMP:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature again and enter it.')
    temperature = float(input('Enter the new celsius temperature:'))
#Remain the user to check  the temperature again in 15 minutes
print('The temperature is acceptable.')
print('check it again in 15 minutes')