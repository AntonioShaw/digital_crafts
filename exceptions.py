
try: 
    result = 1/5
    number = int(input("Enter number: ")) 
    database.open()
    a = 1/0
# zero division exception block 
except ZeroDivisionError: 
    print("Divided by ZERO!")
except ValueError:
    print("Please input only numbers!")
except: 
    print("Opps something bad happened!")
#Optional block. Fired when no exceptions are thrown
else:
    print("ELSE BLOCK")
#Optional. "finally" block is fired no matter what. This means it fired
#whether or not the exception happens.
#finally is used to clean up the resources
#close database connections, file connections, socket connections
finally:
    print("FINALLY")
    database.close()
    