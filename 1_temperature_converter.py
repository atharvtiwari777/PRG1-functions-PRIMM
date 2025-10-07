def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celcius = (fahrenheit - 32) / 1.8
    return celcius


# Test the function
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(20))
print(celsius_to_fahrenheit(100))
print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(68))
print(fahrenheit_to_celsius(212))