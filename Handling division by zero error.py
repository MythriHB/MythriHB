try:
  num1=int(input("enter numerator:"))
  num2=int(input("enter denominator:"))
  result=num1/num2
  print("result:",result)
except zerodivisionerror:
  print("error:cannot divide by zero.")
except valueerror:
  print("invalid input!enter numeric values.")
