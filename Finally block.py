try:
  file = open("/content/Mythri gowda.txt","r")
except filenotfounderror:
  print("file not found.")
finally:
   print("execution complete.")
