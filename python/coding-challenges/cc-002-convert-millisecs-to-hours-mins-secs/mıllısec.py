def Convert_Miliseconds( num):
    hour=0
    minute=0
    second=0
    # if num < 1000 then its only miliseconds
    if num<1000 :
        return "just {} millisecond/s ".format(num)
    num=num//1000   # now its only seconds
    result=""
    hour=(num // 3600)
    if hour>0:
        result="{} hour/s ".format(hour)
        num %= 3600
    minute=(num // 60)
    if minute>0:
        result+="{} minute/s ".format(minute)
        num %= 60
    if num>0:
        result+="{} second/s ".format(num)
    return result
print("###  This program converts milliseconds into hours, minutes, and seconds ###")
print('(To exit the program, please type "exit" )')
condition=True
while True :
    try:
        Input_Text=input("Please enter the milliseconds (should be greater than zero) : ")
        Number = int(Input_Text )
        if Number>0 :
            print(Convert_Miliseconds(Number))
        else:
            print("The input should be a decimal number greater then zero")
    except ValueError:
        if Input_Text.lower() == "exit":
            print("Exiting the program... Good Bye")
            break
        else:
            print("Your input contains string and can not be converted to decimal number. Please Try again")