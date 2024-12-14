#Reading and writing to a file

with open("/content/Mythri gowda.txt","w")as file:
  file.write("mythri is a awesome!\n")
with open ("/content/Mythri gowda.txt","r")as file:
  print(file.read())


