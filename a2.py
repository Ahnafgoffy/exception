try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    result = num1 / num2
    print("the reult is:",result)
except ZeroDivisionError:
    print("divvsion by zero in not possible")
except ValueError:
    print("please put valid numbers")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will excecute no matter what")