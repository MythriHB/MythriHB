class NagativeNumberrror(Exception):
  pass

def check_positive(number):
  if number<0:
     raise NegativeNumberError("Negative number entered.")
try:
   num=int(input("Enter a positive number:"))
   check_positive(num)
   print("you entered a positive number.")
except NagativeNumbererror as e:
   print(e)
