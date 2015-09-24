'''

File name           WindChillIndex.py
Description         This program calculates "feels like" temperature
                    based on temperature and wind speed
Author              Jaken Herman
Date                September 8, 2015
Professor           Dr. Ji
Class               Python

'''


temperature_celsius = input('Enter the air temperature in celsius: ') #degrees input to celsius
wind_speed_kph = input('Enter the wind speed in Kilometers per hour: ') #degrees input to kph

fahrenheit = (temperature_celsius * (9.0 / 5.0) + 32)
mph = wind_speed_kph / 1.609344

wind_chill_fahrenheit = round(35.74 + (0.6215 * fahrenheit) - (35.75 * (mph ** 0.16)) + ((0.4275 * fahrenheit) * (mph ** 0.16)))
wind_chill_celsius = round((wind_chill_fahrenheit - 32) * 5/9)

print("It feels like " + str(wind_chill_fahrenheit) + " degrees in Fahrenheit and " + str(wind_chill_celsius) + " degrees in celsius")
