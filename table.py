strt = int(input ("Enter the starting number : "))
end = int(input ("Enter the ending number : "))
for table_num in range(strt,end+1):
    print("************************************")
    for num in range(1,11):
        print(str(table_num) + " x " + str(num) + " = " + str(table_num*num))