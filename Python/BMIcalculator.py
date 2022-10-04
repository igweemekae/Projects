# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(height / (weight ** 2))

if BMI < 18.5:
    print(f"Your BMI is {BMI} and You are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI} and Hey You have a normal weight")
elif BMI< 30:
    print(f"Your BMI is {BMI} and Watch it! You are slightly overweight!")
elif BMI< 35:
    print(f"Your BMI is {BMI} and Oops! You are obese!")
else:
    print("Am afraid! You are clinically obese!")
