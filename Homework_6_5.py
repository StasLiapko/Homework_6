string = input("Please enter a string ")
x = string.split()
max_length = 0
res = ""
for i in x:
    if len(i) > max_length:
        max_length = len(i)
        res = i
print(res)