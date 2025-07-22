dis = int(input("Enter distance:"))

if dis < 5:
    print("Not send")
elif 50 >= dis >= 5:
    print(" 10 baht")
elif 100 >= dis >= 51:
    print(" 15 baht")
elif 300 >= dis >= 101:
    print(" 25 baht")    
elif 500 >= dis >= 301:
    print(" 35 baht")
elif dis > 500:
    print(" 45 baht")