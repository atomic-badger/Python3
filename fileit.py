# OPENS FILE
with open("file_text.txt") as file:
    print(file.read())
    
# REWRITES FILE
with open("tombaker.txt",'w') as f:
   f.write("Tom Baker\n")
   f.write("is my\n")
   f.write("favorite Doctor.\n")   
  
# SOMEWHAT REWRITES FILE - HAPPENS FAST!
with open("tombaker.txt",'w') as f:
   f.write("Sylvester McCoy\n")   
   f.write("is my\n")
   f.write("favorite Doctor.\n")  
   
# APPENDS LAST LINE   
with open("tombaker.txt", "a") as f:
   f.write("end of text.")
   
# REWRITES TOP LINE
with open("tombaker.txt",'w') as f:
   f.write("Matt Smith\n")   
   f.write("is my\n")
   f.write("favorite Doctor.\n")   
   
with open("tombaker.txt") as file:
    print(file.read())
    
with open("some_text.txt") as file:
    print(file.read())
