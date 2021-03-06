from __future__ import print_function

while True:
  try:
    print("Let us solve the equation (x/2) / (x-y) ")
    print("Please enter 0 to exit")

    x = float(input("Please enter a value for x: "))
    y = float(input("Please enter a value for y: "))

    if x==0 or y==0:
      break

    z = (x/2) / (x-y)

    print("Solving (x/2) / (x-y) for values x=", \
      x,"and y=",y,"we get the result",z)
  except ZeroDivisionError as e:
    print("There was an error with the code...")
    print("The equation resulted in a division by zero.")
  except NameError as e:
    print("There was an error with the code...")
    print("You entered a text value where a number was expected.", str(e))
  except Exception as e:
    print("There was an error with the code...")
    print("Error caused by:", str(e))

