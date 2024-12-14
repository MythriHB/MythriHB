try:
  num=int(input("enter a number:"))
  print(10/num)
except zerodivisionError:
  print("cannot divide by zero.")
except valuEerror:
  print("invalid input! please enter a number")
