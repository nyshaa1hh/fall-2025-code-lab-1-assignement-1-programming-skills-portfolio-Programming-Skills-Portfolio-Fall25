num_month = int(input("Enter Month (1-12): "))
if num_month == 2:
    if input("is it Leap year? (yes/no): ") == 'yes':
        print("29 days")
    else:
        print("28 days")
elif num_month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif num_month in [4, 6, 9, 11]:
    print("30 days")
else:
    print("Invalid month")