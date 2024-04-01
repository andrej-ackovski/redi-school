#Even or odd
num_1 = int(input("Enter a number 1 to check if it is even or odd: "))
num_2 = int(input("Enter a number 2 to check if it is even or odd: "))
if num_1 % 2 == 0 and num_2 % 2 == 0:
    print("True")
if num_1 % 2 != 0 and num_2 % 2 != 0:
    print("True")
if num_1 % 5 == 0 or num_2 % 5 == 0:
    print("Number is multiple of 5!")
else:
    print("False")

#Personal weather assistant
temperature_today = int(input("Enter the temperature: "))
if temperature_today < 12 and temperature_today > 8:
    print("Please wear a jacket. ")
elif temperature_today < 4:
    print("Please wear a pair of gloves. ")
elif temperature_today < 8 and temperature_today > 4:
    print("Please wear a scarf. ")
elif temperature_today > 25:
    print("Please wear sunglasses. ")
else:
    print("Enjoy your day! ")

#BBQ
cooking_time = int(input("Cooking time: "))
if cooking_time < 2:
    print("The steak is rare. ")
elif cooking_time >= 2 and cooking_time <= 4:
    print("The steak is perfect. ")
elif cooking_time > 4 and cooking_time <= 8:
    print("The steak is well done. ")
else:
    print("You ruined the steak, your friend is furious! ")
