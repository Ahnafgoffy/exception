try:
    number = int(input("Enter a number: "))
    print("the number you enetered is:",number)
except ValueError as ex:
    print("exception",ex)
    