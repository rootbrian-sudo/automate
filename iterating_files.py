#making a whole line uppercase before printing
with open("new.txt") as file:
    for line in file:
        print(line.strip().upper()) # strip to remove all surrounding white space, including tabs and new lines
        
  
  # Sorting the file
file = open ("new.txt")
lines=file.readlines()  #Creating a variable to hold the line generated by readline(). Accessible even if the file is closed
file.close()
lines.sort() #sorting the lines
print(lines) #  to display a character that's not printable, Python uses escape sequences with backslash, like \n. Another common escape sequence is \t, for tab.






