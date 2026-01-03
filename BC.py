# Budget-Calculator
print("MONTHLY BUDGET TRACKER")
print("="*40)
Monthly_Income = int(input("What is your monthly Income?"))
print("₹", Monthly_Income)
Rent = int(input("What is your Rent?"))
print("Monthly Rent =", "₹", Rent)
Food_Expenses = int(input("What is your Food Expenses?"))
print("Monthly Food Expenses =", "₹", Food_Expenses)
Transport_Expenses = int(input("What is your Transport Expenses?"))
print("Monthly Transport Expenses =", "₹", Transport_Expenses)

print("="*40) ;
print("="*40)

print("FINANCIAL SUMMARY")
print("="*40)
print("Monthly Income =", "₹", Monthly_Income)
Total_Expenses = Rent + Food_Expenses + Transport_Expenses
print("Total Expenses =", "₹", Total_Expenses)
Total_Savings = Monthly_Income - Total_Expenses
print("Total Savings =", "₹", Total_Savings)
print("="*40)
print("Your savings is", int(Total_Savings/Monthly_Income*100), "% of your monthly income")
print("Your expenses are", int(Total_Expenses/Monthly_Income*100), "% of your monthly income")

print("="*40)
print("RECOMMENDATION")
print("="*40)
if Total_Savings > Monthly_Income*0.5:
  print("YOU ARE SAVING WELL, NOW YOU SHOULD INVEST")
elif Total_Savings > 0:
  print("YOU ARE SAVING BUT YOU COULD SAVE MORE")
elif Total_Savings == 0:
  print("YOU REALLY NEED TO SAVE MONEY")
elif Total_Savings < 0:
  print("YOU ARE IN DEBT")

if Total_Expenses > Monthly_Income:
  print("YOU ARE SPENDING WAY TOO MUCH, YOU MAY GO IN DEBT")
elif Total_Expenses > Monthly_Income*0.5:
  print("YOU ARE SPENDING MORE THAN 50% OF YOUR MONTHLY INCOME")
elif Total_Expenses > Monthly_Income*0.25:
  print("YOU ARE SPENDING AN ALRIGHT AMOUNT")
elif Total_Expenses == 0:
  print("YOU ARE SPENDING NOTHING")
