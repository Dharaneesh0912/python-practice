food=int(input("Enter food expense:"))
travel=int(input("Enter travel expense:"))
education=int(input("Enter education expense:"))
other=int(input("Enter other expense:"))
total_expense=food+travel+education+other
total_budget=10000
remaining=total_budget-total_expense
if(remaining<0):
    print("Budget exceeded!")
else:
    print("Remaining Budget:",remaining)
