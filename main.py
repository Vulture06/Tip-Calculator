#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
a=input("What was the total bill: $")
b=input("What percentage tip would you like to give? 10,12 or 15? ")
c=input("How many people to split the bill? ")
a_1=int(a)
b_1=int(b)
c_1=int(c)
final=(a_1/c_1)*(1+(b_1/100))
final_1=round(final,2)
print(f"Each person should pay: ${final_1}")