expenses = {
    "food": 2000,
    "travel": 1000,
    "education": 500,
    "other": 300
}
pursue=5000
for key,value in expenses.items():
    pursue-=value
    print(key,":",value)
print("Remaining amount:",pursue)
