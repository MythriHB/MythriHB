def check_age(age):
  if age<18:
    raise valueerror("age must be 18 or older.")
  return true

  try:
    check_age(16)
  except valueerror as e:
    print(e)
