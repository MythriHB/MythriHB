number = int(input("enter a number:"))
reverse_number = 0
temp = number
while temp > 0:
  digit = temp % 10
  reverse_number = reverse_number * 10 + digit
  temp = temp // 10
if number == reverse_number:
    print(f" {number} is a palindrome")
else:
     print(f"{number} is not a palindrome")



number = input("enter a  number:")
if str(number) == str(number)[::-1]:
  print("palindrome")
else:
  print("not palindrome")




number = input("enter a number:")
if (number) == (number)[::-1]:
  print("palindrome")
else:
  print("not palindrome")