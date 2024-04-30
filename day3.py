#booleans
print(10>9)
#booleans are used to evaluate expressions and conditions in python
#used to check if expression is true or false
broughtFood = True
print(broughtFood)

#is_raining = True
#if is_raining:
    #print("Take an umbrella!")
#else:
    #print("No umbrella nedded.")

temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("it's cold")
    print("Done")

age = 22
#if age >= 18:
 #   message = "Eligible"
#else: 
#    message = "Not eligible"

message = "Eligible" if age >= 18 else "Not eligible"
print(message)

high_income = True
good_credit = True
student = True
if high_income or good_credit or not student:
    print("Eligible")


#age should be between >= 18 and age < 65
    age= 22
   # if age >= 18 and age < 65:
    if 18 <= age < 65:
        print("Eligible")


if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")