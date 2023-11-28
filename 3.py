penny= 1
nickel= 5
dime= 10
quarter= 25
pennies_dollar= 100


p = int(input("Enter no. of pennies:"))
n = int(input("Enter no. of nickels:"))
d = int(input("Enter no. of dimes:"))
q = int(input("Enter no. of quarters:"))

total= (p*penny) + (n*nickel) + (d*dime) + (q*quarter)

    
final_dollar= total/pennies_dollar

if final_dollar ==1:
        print("Congratulations Champ!")
        print("The amount you entered was exactly one dollar $")
        print("You are the Champion!")
       
elif final_dollar > 1:
        print("Sorry! The amount you entered was more than an dollar.")
elif final_dollar < 1:
        print("Sorry! The amount you entered was less than an dollar.")
    

