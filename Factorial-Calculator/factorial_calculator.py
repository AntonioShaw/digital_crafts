# Write an app which asks users for the input and then prints the factorial for that number.

# Define a fuction that provides a number's factorial.
def factorial(user_input):
  if user_input==0:
    print("The factorial of 0 is 1.")
  elif user_input < 0:
    print("Negative numbers do not have factorials.")
  else:
    factorial=1
    while (user_input>1):
      factorial*=user_input
      user_input-=1  
    print(factorial)# If this is nested under 'while', all factorials within the loop will be displayed in order instead of just the final factorial.

# Receive user input.
number=int(input("Enter a number: "))

factorial(number)