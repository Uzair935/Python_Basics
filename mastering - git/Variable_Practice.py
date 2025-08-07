'''
var1 = 5
var2 = 6

var1,var2 = var2,var1

print(f"  Var1 value is now: {var1}")
print(f"  Var2 value is now: {var2}")
'''

def temp_conversion():
    while True:
        try:
            temp = float(input("What is the temperature (without unit): "))
            break
        except ValueError:
            print("Invalid input! Please enter a number!")
    
    unit = input("What's the unit (C for Celsius,F for Fahrenheit,Q to quit): ")
    if unit.capitalize() == 'C':
        t : float = 1.8*temp + 32
        print(f"Temperature in Fahrenheit: {t}F")
    elif unit.capitalize() =='F':
        t : float = (temp - 32) * 5 / 9
        print(f"Temperature in Celsius: {t}C")
    elif unit.capitalize() =='Q':
        print()
    else:
            print("Invalid input")

temp_conversion()


