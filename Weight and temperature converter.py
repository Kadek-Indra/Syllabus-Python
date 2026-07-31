print ("Converter Weight and Temperature")
WOT = input("Wanna Convert Weight or Temperature? W / T : ")

if WOT == "W":
    unit1 = input("Convert to Kilograms or Pounds? K / P : ")
    weight = float(input("Enter your weight : "))
    if unit1 == "P":
        weight = weight * 2.205
        unit1 = ("Lbs.")
        print (f"The result is : {weight} {unit1}")
    elif unit1 == "K":
        weight = weight / 2.205
        unit1 = ("Kgs.")
        print (f"The result is : {weight} {unit1}")
    else:
        print ("your unit was not right")
elif WOT == "T":
    unit2 = input("Convert to Celcius or Fahrenhit? C /F : ")
    temp = float(input("Enter the temperature : "))
    if unit2 == "F":
        temp = round((9 * temp) / 5 + 32, 1)
        unit2 = "F"
        print (f"The temperature in Fahrenheit is : {temp} {unit2}")
    elif unit2 == "C":
        temp = round((temp - 32) * 5 / 9, 1)
        unit2 = "C"
        print (f"The temperature in Celsius is : {temp} {unit2}")
    else:
        print ("your unit was not right")
else:
    print ("Enter the right convert")
