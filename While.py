user_num = int(input("Please enter a number:"))
avrg = 0
count = 0
while user_num != -1:
    avrg += user_num
    count += 1
    user_num = int(input("Please enter a number:"))
print(str(round(avrg/count,2)))