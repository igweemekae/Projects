# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_ = int(age)

age_now = 90 - age_

age_months = int(age_now * 12)

age_weeks = int(age_now * 52)

age_days = int(age_now * 365)

print(f"You have {age_days}days, {age_weeks}weeks, and {age_months}months left.")
