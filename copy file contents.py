with open("/content/Mythri gowda.txt","r")as source_file:
    data=source_file.read()
with open("/content/images.jpeg","w")as dest_file:
  dest_file.write(data)
print("file copied successfully!")
