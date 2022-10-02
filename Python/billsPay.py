#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("welcome to the tip calculator!!!")

bill = float(input ("What is the amount you incured?"))

tip = float(input("How much % tip are you giving?"))

people = int(input("how many persons will incure the cost?"))

tipBills = tip / 100 * bill + bill

billperPerson = tipBills / 5

print(f"The amount you will pay as tip is {tipBills} and each person will pay {billperPerson}")