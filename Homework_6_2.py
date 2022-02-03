Temp = '0123456789.+-/=*'
x = input("Input surname:")
for i in x:
    if i in Temp:
        print("Your surname contains forbidden signs")
        break
    elif x.istitle() is False:
        print("Check first letter")
        break
else:
    print("Correct")
